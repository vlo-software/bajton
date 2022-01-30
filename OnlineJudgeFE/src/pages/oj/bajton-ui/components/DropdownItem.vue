<template>
  <li :class="classes" @click="handleClick"><slot></slot></li>
</template>
<script>
export default {
  name: 'DropdownItem',
  props: {
    name: {
      type: [String, Number]
    },
    disabled: {
      type: Boolean,
      default: false
    },
    selected: {
      type: Boolean,
      default: false
    },
    divided: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    classes () {
      return [
        `main`,
        {
          [`disabled`]: this.disabled,
          [`selected`]: this.selected,
          [`divided`]: this.divided
        }
      ] // TODO: Implement these classes
    }
  },
  methods: {
    findComponentUpward (context, componentName, componentNames) {
      if (typeof componentName === 'string') {
        componentNames = [componentName]
      } else {
        componentNames = componentName
      }

      let parent = context.$parent
      let name = parent.$options.name
      while (parent && (!name || componentNames.indexOf(name) < 0)) {
        parent = parent.$parent
        if (parent) name = parent.$options.name
      }
      return parent
    },
    handleClick () {
      const $parent = this.findComponentUpward(this, 'Dropdown')
      const hasChildren =
        this.$parent && this.$parent.$options.name === 'Dropdown'

      if (this.disabled) {
        this.$nextTick(() => {
          $parent.currentVisible = true
        })
      } else if (hasChildren) {
        this.$parent.$emit('on-haschild-click')
      } else {
        if ($parent && $parent.$options.name === 'Dropdown') {
          $parent.$emit('on-hover-click')
        }
      }
      $parent.$emit('on-click', this.name)
    }
  }
}
</script>

<style lang="less" scoped>
.main {
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
  font-size: 1em;
  line-height: normal;
  list-style-type: none;
  margin: 2px;
  padding: 11px 36px 11px 11px;
  border-radius: 8px;
  color: var(--text-color);
  transition: 0.2s ease;
  &:hover {
    background: var(--background-color-full);
  }
}
</style>
