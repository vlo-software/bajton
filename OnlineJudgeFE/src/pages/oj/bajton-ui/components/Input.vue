<template>
  <div class="input-wrapper">
    <form @submit="submit">
      <input
        ref="input"
        :placeholder="placeholder"
        :class="classes"
        :value="value"
        :type="type"
        @input="handleInput"
      />
    </form>
    <i
      v-if="icon"
      @click="() => this.submit({ preventDefault: () => {} })"
      :class="`bi icon bi-${icon}`"
    />
  </div>
</template>

<script>
export default {
  name: 'Input',
  props: {
    value: {
      type: String,
      required: true
    },
    class: {
      type: String
    },
    icon: String,
    placeholder: String,
    type: {
      type: String,
      default: 'text'
    }
  },
  methods: {
    submit (e) {
      e.preventDefault()
      const value = this.$refs.input.value
      this.$emit('input', value)
      this.$emit('on-enter', value)
      this.dispatch('FormItem', 'on-form-change', value)
    },
    handleInput (e) {
      const value = this.$refs.input.value
      this.$emit('input', value)
      this.dispatch('FormItem', 'on-form-change', value)
      this.$emit('on-change', e)
    },
    dispatch (componentName, eventName, params) {
      let parent = this.$parent || this.$root
      let name = parent.$options.name

      while (parent && (!name || name !== componentName)) {
        parent = parent.$parent

        if (parent) {
          name = parent.$options.name
        }
      }
      if (parent) {
        parent.$emit.apply(parent, [eventName].concat(params))
      }
    }
  },
  computed: {
    classes () {
      return [
        `input`,
        {
          // TODO: Add support for other styles (size)
        }
      ]
    }
  }
}
</script>

<style lang="less" scoped>
.input {
  background: var(--background-color-panel);
  outline: none;
  border: none;
  border-radius: 10px;
  color: var(--text-color);
  font-size: 1em;
  font-weight: 600;
  appearance: none;
  padding: 6px 10px;
  width: 100%;
  height: 2.67em !important;
  cursor: pointer;
}
.input-wrapper {
  position: relative;
  width: 160px;
  height: 2.67em;
}
.icon {
  position: absolute;
  right: 10px;
  top: 4px;
  line-height: 2.67em;
  cursor: pointer;
}
</style>
