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
    <div
      v-if="loading"
      style="
        position: absolute;
        text-align: center;
        left: calc(50% - 7px);
        top: calc(50% - 7px);
        width: 14px;
        height: 14px;
        background: white;
        border-radius: 100%;
        animation: fade 1s ease infinite;
      "
    ></div>
    <span
      class="btn-slot"
      v-if="showSlot"
      :style="loading ? `opacity: 0` : `opacity: 1`"
      ref="slot"
      ><slot></slot
    ></span>
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
          [`btn-icon-only`]: !this.showSlot && (!!this.icon || this.loading),
          [`btn-disabled`]: !!this.disabled
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

<style>
@keyframes fade {
  0% {
    opacity: 0;
  }
  50% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}
</style>

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
  &-slot {
    transition: opacity 75ms ease-in-out;
    white-space: nowrap;
  }
  &-small {
    padding: 8px 10px;
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
    color: #fff;
    border: none;
  }
  &-ghost {
    background: transparent;
  }
  &-dashed {
    background: var(--dashed-color);
    color: #fff;
  }
  &-text {
    background: transparent;
    border: none;
  }
  &-info {
    background: var(--info-color);
    color: #fff;
    border: none;
  }
  &-success {
    background: var(--success-color);
    color: #fff;
    border: none;
  }
  &-warning {
    background: var(--warning-color);
    color: #fff;
    border: none;
  }
  &-error {
    background: var(--error-color);
    color: #fff;
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
  &-disabled {
    cursor: not-allowed;
    &:hover {
      filter: none;
    }
  }
}
</style>
