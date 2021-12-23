<template>
  <span class="select-wrapper">
    <select @change="change" :value="selectValue" :class="classes">
      <slot></slot>
    </select>
  </span>
</template>

<script>
export default {
  name: 'Select',
  props: {
    value: {
      type: String,
      required: true
    },
    class: {
      type: String
    },
    expand: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return { selectValue: this.value }
  },
  methods: {
    change (e) {
      this.selectValue = e.target.value
      this.$emit('input', e.target.value)
      this.$emit('on-change', e.target.value)
    }
  },
  computed: {
    classes () {
      return [
        `select`,
        {
          expand: !!this.expand
          // TODO: Add support for other styles (size, icon)
        }
      ]
    }
  }
  // TODO: Add support for search
}
</script>

<style lang="less" scoped>
.select {
  background: var(--background-color-panel);
  outline: none;
  border: none;
  border-radius: 10px;
  color: var(--text-color);
  padding: 6px 12px;
  font-size: 1em;
  font-weight: 600;
  appearance: none;
  width: 160px;
  cursor: pointer;
}
.expand {
  width: 100%;
}
.select-wrapper {
  position: relative;
  &:after {
    content: '\25BC';
    position: absolute;
    top: 0px;
    right: 10px;
    font-size: 1em;
    line-height: 1.2em;
    opacity: 0.3;
    cursor: pointer;
    transition: 0.2s ease;
  }
  &:hover {
    &:after {
      opacity: 0.5;
    }
  }
}
</style>
