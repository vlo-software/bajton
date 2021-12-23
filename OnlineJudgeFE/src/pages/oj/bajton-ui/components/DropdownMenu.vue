<template>
  <ul class="menu">
    <slot></slot>
  </ul>
</template>

<script>
export default {
  name: 'DropdownMenu'
}
</script>

<style lang="less" scoped>
.menu {
  min-width: 100px;
}
</style>
