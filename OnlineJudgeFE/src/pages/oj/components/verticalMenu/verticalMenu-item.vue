<template>
  <li @click.stop="handleClick" :class="{ disabled: disabled }">
    <slot></slot>
  </li>
</template>

<script>
import Emitter from '../mixins/emitter'

export default {
  name: 'VerticalMenu-item',
  mixins: [Emitter],
  props: {
    route: {
      type: [String, Object]
    },
    disabled: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    handleClick () {
      if (this.route) {
        this.dispatch('VerticalMenu', 'on-click', this.route)
      }
    }
  }
}
</script>

<style scoped lang="less">
.disabled {
  /*background-color: #ccc;*/
  opacity: 1;
  /*cursor: not-allowed;*/
  pointer-events: none;
  color: var(--diff-tone-color);
  &:hover {
    border-left: none;
    color: var(--diff-tone-color);
    background: var(--background-color-full);
  }
}

li {
  color: var(--text-color);
  display: block;
  text-align: left;
  padding: 15px 20px;
  border-radius: 10px;
  cursor: pointer;
  transition: 0.2s ease;
  &:hover {
    border-left: 2px solid var(--primary-color);
    background: var(--pre-background-color);
    color: var(--primary-color);
  }
  & > .ivu-icon {
    font-size: 16px;
    margin-right: 8px;
  }
  &:last-child {
    border-bottom: none;
  }
}
</style>
