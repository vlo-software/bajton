<template>
  <option :value="value"><slot></slot></option>
</template>

<script>
export default {
  name: 'Option',
  props: {
    value: String
  }
}
// TODO: Make this not stock (looks wise)
</script>

<style lang="less" scoped>
option {
  background: var(--background-color-panel);
  line-height: 2em;
}
</style>
