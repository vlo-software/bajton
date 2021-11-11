<template>
  <div :class="classes">
    <slot></slot>
    <span class="tiptext">{{ content }}</span>
  </div>
</template>

<script>
export default {
  name: 'Tooltip',
  props: {
    content: String,
    placement: {
      validator (value) {
        return ['top', 'bottom', 'left', 'right'].includes(value)
      }
    }
  },
  computed: {
    classes () {
      return [
        `tooltip`,
        {
          [this.placement]: !!this.placement
        }
      ]
    }
  }
}
</script>

<style lang="less" scoped>
.tooltip {
  position: relative;
  display: inline-block;
}
.tooltip .tiptext {
  visibility: hidden;
  width: 180px;
  background-color: var(--background-color-panel);
  color: var(--text-color);
  opacity: 0.9;
  text-align: center;
  border-radius: 10px;
  padding: 6px 10px;
  position: absolute;
  z-index: 100;
}
.tooltip .tiptext::after {
  content: '';
  position: absolute;
  border-width: 5px;
  border-style: solid;
}
.tooltip:hover .tiptext {
  visibility: visible;
}

.tooltip.top .tiptext {
  margin-left: -90px;
  bottom: 130%;
  left: 50%;
}
.tooltip.top .tiptext::after {
  margin-left: -5px;
  top: 100%;
  left: 50%;
  border-color: var(--background-color-panel) transparent transparent
    transparent;
}

.tooltip.bottom .tiptext {
  margin-left: -90px;
  top: 130%;
  left: 50%;
}
.tooltip.bottom .tiptext::after {
  margin-left: -5px;
  bottom: 100%;
  left: 50%;
  border-color: var(--background-color-panel) transparent transparent
    transparent;
}

.tooltip.left .tiptext {
  top: -5px;
  right: 110%;
}
.tooltip.left .tiptext::after {
  margin-top: -5px;
  top: 50%;
  left: 100%;
  border-color: var(--background-color-panel) transparent transparent
    transparent;
}

.tooltip.right .tiptext {
  top: -5px;
  left: 110%;
}
.tooltip.right .tiptext::after {
  margin-top: -5px;
  top: 50%;
  right: 100%;
  border-color: var(--background-color-panel) transparent transparent
    transparent;
}
</style>
