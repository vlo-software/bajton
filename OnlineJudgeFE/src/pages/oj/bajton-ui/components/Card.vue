<template>
  <div class="main">
    <div class="head" v-if="showHead">
      <slot name="title">
        <p v-if="title">
          {{ title }}
        </p>
      </slot>
      <div v-if="showExtra"><slot name="extra"></slot></div>
    </div>
    <div>
      <div :style="bodyStyles"><slot></slot></div>
    </div>
  </div>
</template>

<script>
const defaultPadding = 16

export default {
  name: 'Card',
  props: {
    padding: {
      type: Number,
      default: defaultPadding
    },
    title: {
      type: String
    }
  },
  data () {
    return {
      showHead: true,
      showExtra: true
    }
  },
  computed: {
    bodyStyles () {
      if (this.padding !== defaultPadding) {
        return {
          padding: `${this.padding}px`
        }
      } else {
        return ''
      }
    }
  },
  mounted () {
    this.showHead = this.title || this.$slots.title !== undefined
    this.showExtra = this.$slots.extra !== undefined
  }
}
</script>

<style lang="less" scoped>
.head {
  width: calc(100% - 40px);
  height: 60px;
  margin-left: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  p {
    font-size: 2.5em !important;
  }
}
.main {
  display: grid;
  border-radius: 10px;
  background: var(--background-color-full);
  font-size: 1.2em;
}
</style>
