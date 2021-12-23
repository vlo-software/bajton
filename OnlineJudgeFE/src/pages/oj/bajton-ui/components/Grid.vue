<template>
  <div :style="`${style}; grid-gap: ${gap}px`" :class="classes">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: 'Grid',
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
    direction: {
      type: String,
      validator (value) {
        return ['row', 'column'].includes(value)
      },
      default: 'row'
    },
    gap: {
      type: Number,
      default: 0
    },
    style: String
  },
  computed: {
    classes () {
      return [
        `grid-main`,
        {
          'grid-justify-start': this.justify === 'start',
          'grid-justify-center': this.justify === 'center',
          'grid-justify-between': this.justify === 'between',
          'grid-justify-evenly': this.justify === 'evenly',
          'grid-justify-around': this.justify === 'around',
          'grid-justify-end': this.justify === 'end',
          'grid-align-start': this.align === 'start',
          'grid-align-center': this.align === 'center',
          'grid-align-end': this.align === 'end',
          'grid-wrap': this.wrap,
          'grid-direction-row': this.direction === 'row',
          'grid-direction-column': this.direction === 'column'
        }
      ]
    }
  }
}
</script>

<style lang="less" scoped>
.grid-main {
  display: flex;
}
.grid-justify-start {
  justify-content: flex-start;
}
.grid-justify-center {
  justify-content: center;
}
.grid-justify-between {
  justify-content: space-between;
}
.grid-justify-evenly {
  justify-content: space-evenly;
}
.grid-justify-around {
  justify-content: space-around;
}
.grid-justify-end {
  justify-content: flex-end;
}
.grid-align-start {
  align-items: flex-start;
}
.grid-align-center {
  align-items: center;
}
.grid-align-end {
  align-items: flex-end;
}
.grid-wrap {
  flex-wrap: wrap;
}
.grid-direction-row {
  flex-direction: row;
}
.grid-direction-column {
  flex-direction: column;
}
</style>
