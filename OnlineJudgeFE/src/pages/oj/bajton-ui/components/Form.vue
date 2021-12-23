<template>
  <form :class="classes" :autocomplete="autocomplete"><slot></slot></form>
</template>
<script>
export default {
  name: 'Form',
  props: {
    model: {
      type: Object
    },
    rules: {
      type: Object
    },
    labelWidth: {
      type: Number
    },
    labelPosition: {
      validator (value) {
        return ['left', 'right', 'top'].includes(value)
      },
      default: 'right'
    },
    inline: {
      type: Boolean,
      default: false
    },
    showMessage: {
      type: Boolean,
      default: true
    },
    autocomplete: {
      validator (value) {
        return ['on', 'off'].includes(value)
      },
      default: 'off'
    }
  },
  provide () {
    return { form: this }
  },
  data () {
    return {
      fields: []
    }
  },
  computed: {
    classes () {
      return [
        `bajton-ui-form`,
        `bajton-ui-form-label-${this.labelPosition}`,
        {
          [`bajton-ui-form-inline`]: this.inline
        }
      ]
    }
  },
  methods: {
    resetFields () {
      this.fields.forEach((field) => {
        field.resetField()
      })
    },
    validate (callback) {
      return new Promise((resolve) => {
        let valid = true
        let count = 0
        this.fields.forEach((field) => {
          field.validate('', (errors) => {
            if (errors) {
              valid = false
            }
            if (++count === this.fields.length) {
              // all finish
              resolve(valid)
              if (typeof callback === 'function') {
                callback(valid)
              }
            }
          })
        })
      })
    },
    validateField (prop, cb) {
      const field = this.fields.filter((field) => field.prop === prop)[0]
      if (!field) {
        throw new Error(
          '[iView warn]: must call validateField with valid prop string!'
        )
      }

      field.validate('', cb)
    }
  },
  watch: {
    rules () {
      this.validate()
    }
  },
  created () {
    this.$on('on-form-item-add', (field) => {
      if (field) this.fields.push(field)
      return false
    })
    this.$on('on-form-item-remove', (field) => {
      if (field.prop) this.fields.splice(this.fields.indexOf(field), 1)
      return false
    })
  }
}
</script>

<style lang="less" scoped>
.bajton-ui-form {
  .bajton-ui-form-item-label {
    text-align: right;
    vertical-align: middle;
    float: left;
    font-size: 0.9em;
    color: var(--text-color);
    line-height: 1;
    padding: 10px 12px 10px 0;
    box-sizing: border-box;
  }
  &-label-left .bajton-ui-form-item-label {
    text-align: left;
  }
  &-label-top .bajton-ui-form-item-label {
    float: none;
    display: inline-block;
    padding: 0 0 10px 0;
  }
  &-inline {
    .bajton-ui-form-item {
      display: inline-block;
      margin-right: 10px;
      vertical-align: top;
    }
  }
}

.bajton-ui-form-item {
  margin-bottom: 24px;
  vertical-align: top;
  &-content {
    position: relative;
    line-height: 32px;
    font-size: 0.9em;
  }
  & & {
    margin-bottom: 0;
  }
  & & &-content {
    margin-left: 0 !important;
  }

  &-error-tip {
    position: absolute;
    top: 100%;
    left: 0;
    line-height: 1;
    padding-top: 6px;
    color: var(--error-color);
  }

  &-required {
    .bajton-ui-form-item-label:before {
      content: '*';
      display: inline-block;
      margin-right: 4px;
      line-height: 1;
      font-family: SimSun;
      font-size: 0.9em;
      color: var(--error-color);
    }
  }
}
</style>
