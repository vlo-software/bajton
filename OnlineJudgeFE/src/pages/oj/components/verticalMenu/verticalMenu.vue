<template>
  <Card :padding="0" dis-hover>
    <ul>
      <slot></slot>
    </ul>
  </Card>
</template>

<script>
import { Card } from '@oj/bajton-ui'

export default {
  name: 'VerticalMenu',
  components: { Card }
}
</script>

<style scoped lang="less"></style>
