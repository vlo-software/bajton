<template>
  <pre
    v-highlight="code"
    :style="styleObject"
  ><code :class="language" :style="{filter: this.darkMode ? 'invert(1)' : 'invert(0)'}"></code></pre>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'highlight',
  data () {
    return {
      styleObject: {
        'border-left': '2px solid green'
      }
    }
  },
  props: {
    language: {
      type: String
    },
    code: {
      required: true,
      type: String
    },
    borderColor: {
      type: String,
      default: 'green'
    }
  },
  mounted () {
    this.styleObject['border-left'] = '2.5px solid ' + this.borderColor
  },
  watch: {
    borderColor (newVal, oldVal) {
      this.styleObject['border-left'] = '2.5px solid ' + newVal
    }
  },
  computed: {
    ...mapGetters(['darkMode'])
  }
}
</script>

<style scoped lang="less">
pre {
  padding: 0;
  display: block;
  code {
    max-width: calc(80vw - 70px);
    padding: 20px;
    font-size: 1.1em;
  }
}
</style>
