<template>
  <button
    :type="htmlType"
    :class="classes"
    :disabled="disabled"
    @click="handleClick"
  >
    <!-- TODO: Fix this -->
    <!-- <Icon class="ivu-load-loop" type="load-c" v-if="loading"></Icon> -->
    <i style="height: 5px" :class="`bi bi-${icon}`" v-if="icon && !loading"></i>
    <div v-if="loading">...</div>
    <span v-if="showSlot" ref="slot"><slot></slot></span>
  </button>
</template>
<script>
export default {
  name: 'Button',
  props: {
    type: {
      validator (value) {
        return [
          'primary',
          'ghost',
          'dashed',
          'text',
          'info',
          'success',
          'warning',
          'error',
          'default'
        ].includes(value)
      }
    },
    shape: {
      validator (value) {
        return ['circle', 'circle-outline'].includes(value)
      }
    },
    size: {
      validator (value) {
        return ['small', 'large', 'default'].includes(value)
      }
    },
    loading: Boolean,
    disabled: Boolean,
    htmlType: {
      default: 'button',
      validator (value) {
        return ['button', 'submit', 'reset'].includes(value)
      }
    },
    icon: String,
    long: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      showSlot: true
    }
  },
  computed: {
    classes () {
      return [
        `btn`,
        {
          [`btn-${this.type}`]: !!this.type,
          [`btn-long`]: this.long,
          [`btn-${this.shape}`]: !!this.shape,
          [`btn-${this.size}`]: !!this.size,
          [`btn-loading`]: this.loading != null && this.loading,
          [`btn-icon-only`]: !this.showSlot && (!!this.icon || this.loading)
        }
      ]
    }
  },
  methods: {
    handleClick (event) {
      this.$emit('click', event)
    }
  },
  mounted () {
    this.showSlot = this.$slots.default !== undefined
  }
}
</script>

<style scoped lang="less">
.btn {
  box-sizing: border-box;
  border: 1px solid var(--background-color-panel);
  border-radius: 10px;
  padding: 10px 20px;
  line-height: 1em;
  font-size: 1em;
  font-weight: 600;
  color: var(--text-color);
  background: var(--background-color-panel);
  outline: none;
  transition: 0.2s ease;
  cursor: pointer;
  &-small {
    padding: 7px;
    font-size: 0.8em;
    font-weight: 500;
  }
  &-large {
    line-height: 1.2em;
  }
  &-long {
    width: 100%;
  }
  &-circle {
    border-radius: 5000px;
  }
  &-primary {
    background: var(--primary-color);
    border: none;
  }
  &-ghost {
    background: transparent;
  }
  &-dashed {
    background: var(--dashed-color);
  }
  &-text {
    background: transparent;
    border: none;
  }
  &-info {
    background: var(--info-color);
    border: none;
  }
  &-success {
    background: var(--success-color);
    border: none;
  }
  &-warning {
    background: var(--warning-color);
    border: none;
  }
  &-error {
    background: var(--error-color);
    border: none;
  }
  &-default {
    border: none;
  }
  &-icon-only {
    padding: 8px 15px;
  }
  &:hover {
    filter: brightness(110%);
  }
}
</style>
