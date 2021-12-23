<template>
  <div :style="customColor" :class="classes">
    <div v-if="type === 'dot'" class="dot"></div>
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: 'Tag',
  props: {
    type: {
      validator (value) {
        return ['border', 'dot'].includes(value)
      }
    },
    color: String
  },
  computed: {
    classes () {
      return [
        'tag',
        {
          'full-bg': this.type === undefined,
          bordered: this.type === 'border',
          default: this.color === undefined,
          primary: this.color === 'primary',
          success: this.color === 'success',
          error: this.color === 'error',
          warning: this.color === 'warning',
          magenta: this.color === 'magenta',
          red: this.color === 'red',
          volcano: this.color === 'volcano',
          orange: this.color === 'orange',
          gold: this.color === 'gold',
          yellow: this.color === 'yellow',
          lime: this.color === 'lime',
          green: this.color === 'green',
          cyan: this.color === 'cyan',
          blue: this.color === 'blue',
          geekblue: this.color === 'geekblue',
          purple: this.color === 'purple'
        }
      ]
    },
    customColor () {
      return this.color
        ? this.color.startsWith('#')
          ? `--tag-color: ${this.color}`
          : ''
        : ''
    }
  }
}
</script>

<style lang="less" scoped>
.tag {
  background: var(--background-color-panel);
  padding: 8px 15px;
  display: flex;
  align-items: center;
  border-radius: 10px;
  font-weight: 600;
  box-sizing: border-box;
  cursor: pointer;
}
.full-bg {
  background: var(--tag-color);
}
.bordered {
  border: 1px solid var(--tag-color);
}
.dot {
  height: 1em;
  width: 1em;
  border-radius: 100%;
  background: var(--tag-color);
  margin-right: 8px;
}
.default {
  --tag-color: var(--text-color);
}
.primary {
  --tag-color: var(--primary-color);
}
.success {
  --tag-color: var(--success-color);
}
.error {
  --tag-color: var(--error-color);
}
.warning {
  --tag-color: var(--warning-color);
}
.magenta {
  --tag-color: rgb(235, 47, 150);
}
.red {
  --tag-color: rgb(245, 34, 45);
}
.volcano {
  --tag-color: rgb(250, 84, 28);
}
.orange {
  --tag-color: rgb(250, 140, 22);
}
.gold {
  --tag-color: rgb(250, 173, 20);
}
.yellow {
  --tag-color: rgb(250, 219, 20);
}
.lime {
  --tag-color: rgb(160, 217, 17);
}
.green {
  --tag-color: rgb(82, 196, 26);
}
.cyan {
  --tag-color: rgb(19, 194, 194);
}
.blue {
  --tag-color: rgb(24, 144, 255);
}
.geekblue {
  --tag-color: rgb(47, 84, 235);
}
.purple {
  --tag-color: rgb(114, 46, 209);
}
</style>
