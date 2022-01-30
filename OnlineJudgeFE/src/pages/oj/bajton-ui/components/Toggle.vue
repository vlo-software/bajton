<template>
  <span
    tabindex="0"
    :class="wrapClasses"
    @click="toggle"
    @keydown.space="toggle"
  >
    <input type="hidden" :name="name" :value="currentValue" />
    <span :class="innerClasses">
      <slot name="open" v-if="currentValue === trueValue"></slot>
      <slot name="close" v-if="currentValue === falseValue"></slot>
    </span>
  </span>
</template>
<script>
import Emitter from '../mixins/emitter'

export default {
  name: 'Toggle',
  mixins: [Emitter],
  props: {
    value: {
      type: [String, Number, Boolean],
      default: false
    },
    trueValue: {
      type: [String, Number, Boolean],
      default: true
    },
    falseValue: {
      type: [String, Number, Boolean],
      default: false
    },
    disabled: {
      type: Boolean,
      default: false
    },
    size: {
      validator (value) {
        return ['large', 'small', 'default'].includes(value)
      }
    },
    name: {
      type: String
    }
  },
  data () {
    return {
      currentValue: this.value
    }
  },
  computed: {
    wrapClasses () {
      return [
        `switch`,
        {
          [`switch-checked`]: this.currentValue === this.trueValue,
          [`switch-disabled`]: this.disabled,
          [`switch-${this.size}`]: !!this.size
        }
      ]
    },
    innerClasses () {
      return `switch-inner`
    }
  },
  methods: {
    toggle (event) {
      event.preventDefault()
      if (this.disabled) {
        return false
      }

      const checked =
        this.currentValue === this.trueValue ? this.falseValue : this.trueValue

      this.currentValue = checked
      this.$emit('input', checked)
      this.$emit('on-change', checked)
      this.dispatch('FormItem', 'on-form-change', checked)
    }
  },
  watch: {
    value (val) {
      if (val !== this.trueValue && val !== this.falseValue) {
        throw Error('Value should be trueValue or falseValue.')
      }
      this.currentValue = val
    }
  }
}
</script>

<style lang="less" scoped>
.switch {
  display: inline-block;
  width: 48px;
  height: 22px;
  line-height: 22px;
  border-radius: 5000px;
  vertical-align: middle;
  background-color: var(--background-color);
  position: relative;
  cursor: pointer;
  user-select: none;
  transition: 0.2s ease;

  span {
    opacity: 0.5;
  }

  &-checked span {
    opacity: 1;
  }

  &-inner {
    color: var(--text-color);
    font-size: 0.9em;
    position: absolute;
    left: 25px;

    i {
      width: 12px;
      height: 12px;
      text-align: center;
    }
  }

  &:after {
    content: '';
    width: 22px;
    height: 22px;
    border-radius: 5000px;
    background-color: var(--background-color-panel);
    position: absolute;
    left: 0px;
    top: 0px;
    cursor: pointer;
    transition: 0.2s ease;
  }

  &:active:after {
    width: 26px;
  }

  &-small {
    width: 24px;
    height: 12px;
    line-height: 10px;
    &:after {
      width: 10px;
      height: 10px;
      top: 0;
      left: 0;
    }
    &:active:after {
      width: 14px;
    }
  }

  &-small&-checked:after {
    left: 12px;
  }

  &-small:active&-checked:after {
    left: 8px;
  }

  &-large {
    width: 60px;
    &:active:after {
      width: 26px;
    }
  }

  &-large:active:after {
    width: 35px;
  }

  &-large&-checked:after {
    left: 39px;
  }

  &-large:active&-checked:after {
    left: 27px;
  }

  &-checked {
    border-color: var(--primary-color);
    background-color: var(--primary-color);

    .switch-inner {
      left: 5px;
      right: 20px;
      text-align: center;
      color: #fff;
    }

    &:after {
      left: 27px;
    }

    &:active:after {
      left: 19px;
    }
  }

  &-disabled {
    cursor: no-drop;
    background: var(--background-color-full);

    &:after {
      background: var(--background-color);
      cursor: not-allowed;
    }

    .switch-inner {
      color: var(--background-color);
    }
  }
}
</style>
