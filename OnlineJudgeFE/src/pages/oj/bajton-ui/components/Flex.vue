<template>
  <div :style="style" :class="classes">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: 'Flex',
  props: {
    justify: {
      type: String,
      validator (value) {
        return [
          'start',
          'center',
          'between',
          'evenly',
          'around',
          'end'
        ].includes(value)
      },
      default: 'start'
    },
    align: {
      validator (value) {
        return ['start', 'center', 'end'].includes(value)
      }
    },
    wrap: {
      type: Boolean,
      default: false
    },
    direction: {
      type: String,
      validator (value) {
        return ['row', 'column'].includes(value)
      },
      default: 'row'
    },
    style: String
  },
  computed: {
    classes () {
      return [
        `felx-main`,
        {
          'flex-justify-start': this.justify === 'start',
          'flex-justify-center': this.justify === 'center',
          'flex-justify-between': this.justify === 'between',
          'flex-justify-evenly': this.justify === 'evenly',
          'flex-justify-around': this.justify === 'around',
          'flex-justify-end': this.justify === 'end',
          'flex-align-start': this.align === 'start',
          'flex-align-center': this.align === 'center',
          'flex-align-end': this.align === 'end',
          'flex-wrap': this.wrap,
          'flex-direction-row': this.direction === 'row',
          'flex-direction-column': this.direction === 'column'
        }
      ]
    }
  }
}
</script>

<style lang="less" scoped>
.flex-main {
  display: flex;
}
.flex-justify-start {
  justify-content: flex-start;
}
.flex-justify-center {
  justify-content: center;
}
.flex-justify-between {
  justify-content: space-between;
}
.flex-justify-evenly {
  justify-content: space-evenly;
}
.flex-justify-around {
  justify-content: space-around;
}
.flex-justify-end {
  justify-content: flex-end;
}
.flex-align-start {
  align-items: flex-start;
}
.flex-align-center {
  align-items: center;
}
.flex-align-end {
  align-items: flex-end;
}
.flex-wrap {
  flex-wrap: wrap;
}
.flex-direction-row {
  flex-direction: row;
}
.flex-direction-column {
  flex-direction: column;
}
</style>
