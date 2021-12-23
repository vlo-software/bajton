<template>
  <div class="wrapper">
    <slot></slot>
    <div class="content" :style="margin ? `margin-top: ${margin}px` : ''">
      <slot name="list"></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Dropdown',
  props: {
    margin: Number
  }
}
</script>

<style lang="less" scoped>
.wrapper {
  position: relative;
  display: inline-block;
}

.content {
  display: none;
  position: absolute;
  background: var(--background-color-panel);
  box-sizing: border-box;
  padding: 2px;
  margin-top: -1px;
  border-radius: 10px;
  z-index: 1;
}

.wrapper:hover .content {
  display: block;
}
</style>
