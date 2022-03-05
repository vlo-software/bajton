<template>
  <div class="main">
    <!-- <Logo style="transform: scale(0.7); filter: invert(1)" /> --- Revert to this for a normal logo -->
    <Logo style="transform: scale(0.7)" />
  </div>
</template>

<script>
import Logo from './Logo.vue'

export default {
  name: 'forum-header',
  components: { Logo }
}
</script>

<style lang="less" scoped>
.main {
  height: 100px;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
