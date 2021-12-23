<template>
  <div :class="showSizer ? 'page-wrapper' : ''">
    <Button
      @click="prevPage"
      :disabled="currentValue <= 1"
      icon="chevron-left"
    ></Button>
    <Button>{{ currentValue }} / {{ numberOfPages }}</Button>
    <Button
      @click="nextPage"
      :disabled="currentValue >= numberOfPages"
      icon="chevron-right"
    ></Button>
    <div v-if="showSizer">
      <Select @on-change="changePageSize" expand :value="currentPageSize">
        <Option v-for="item in pageSizeOpts" :key="item" :value="item"
          >{{ item }} / Page</Option
        >
      </Select>
    </div>
  </div>
</template>

<script>
import Button from './Button.vue'
import Select from './Select.vue'
import Option from './Option.vue'

export default {
  name: 'Page',
  components: { Button, Select, Option },
  props: {
    current: {
      type: Number,
      default: 1
    },
    total: {
      type: Number,
      default: 0
    },
    pageSize: {
      type: Number,
      default: 10
    },
    showSizer: {
      type: Boolean,
      default: false
    },
    pageSizeOpts: {
      type: Array,
      default: ['10', '20', '30', '40']
    }
  },
  data () {
    return {
      totalNumberOfElements: this.total,
      currentValue: this.current,
      numberOfPages: 1,
      currentPageSize: this.pageSize,
      showSizer: this.showSizer
    }
  },
  mounted () {
    this.numberOfPages =
      Math.ceil(this.totalNumberOfElements / this.currentPageSize) || 1
  },
  watch: {
    total (val) {
      this.totalNumberOfElements = val
      this.numberOfPages =
        Math.ceil(this.totalNumberOfElements / this.currentPageSize) || 1
    },
    current (val) {
      this.currentValue = val
    },
    pageSize (val) {
      this.currentPageSize = val
    }
  },
  methods: {
    nextPage () {
      this.currentValue++
      this.$emit('update:current', this.currentValue)
      this.$emit('on-change', this.currentValue)
    },
    prevPage () {
      this.currentValue--
      this.$emit('update:current', this.currentValue)
      this.$emit('on-change', this.currentValue)
    },
    changePageSize (newValue) {
      this.currentPageSize = newValue
      this.$emit('on-page-size-change', newValue)
      this.$emit('update:current', 1)
      this.$emit('on-change', 1)
    }
  }
}
</script>

<style lang="less" scoped>
.page-wrapper {
  display: grid;
  grid-template-columns: 50px 70px 50px 95px;
  grid-gap: 10px;
  align-items: center;
}
</style>
