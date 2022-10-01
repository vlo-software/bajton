<template>
  <table v-if="data.length !== 0">
    <thead>
      <tr>
        <th
          v-for="col in columns"
          :class="col.align === 'center' ? 'center' : ''"
          :key="col.key || col.title"
        >
          <render-table-header
            v-if="col.renderHeader !== undefined"
            :column="col"
            :render="col.renderHeader"
          />
          <span v-else>
            {{ col.title }}
          </span>
        </th>
      </tr>
    </thead>
    <tbody>
      <tr
        @click="() => onRowClick(item, idx)"
        v-for="(item, idx) in data"
        :key="item.id"
        :class="classes"
      >
        <td
          v-for="col in columns"
          :style="col.width !== undefined ? `width: ${col.width}px` : ``"
          :class="
            (col.align === 'center' ? 'center' : '') +
            ' ' +
            (item.cellClassName
              ? item.cellClassName[col.key]
                ? item.cellClassName[col.key]
                : ''
              : '')
          "
          :key="col.key || col.title"
        >
          <render-table-cell
            v-if="col.render !== undefined"
            :column="col"
            :row="item"
            :index="idx"
            :render="col.render"
          />
          <b v-else-if="col.type === 'index'">
            {{ idx + 1 }}
          </b>
          <span v-else>
            {{ item[col.key] }}
          </span>
        </td>
      </tr>
    </tbody>
  </table>
  <div class="no-data" v-else>{{ noDataText }}</div>
</template>

<script>
import RenderTableCell from './RenderTableCell.vue'
import RenderTableHeader from './RenderTableHeader.vue'
import Button from './Button.vue'
export default {
  components: { Button, RenderTableCell, RenderTableHeader },
  name: 'Table',
  props: {
    columns: Array,
    data: Array,
    noDataText: {
      type: String,
      default: 'No data'
    },
    disabledHover: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    onRowClick (row, idx) {
      this.$emit('on-row-click', row, idx)
    }
  },
  computed: {
    classes () {
      return [
        {
          hover: !this.disabledHover
        }
      ]
    }
  }
}
// TODO: Add loading
</script>

<style lang="less" scoped>
table {
  font-size: 1em !important;
  margin-bottom: 10px;
  border-collapse: collapse;
}
thead {
  background-color: var(--background-color-panel);
}
th {
  text-align: start;
}
th,
td {
  padding: 10px 18px;
}

.hover {
  &:hover {
    background: var(--background-color);
  }
}

div.no-data {
  width: 100%;
  height: 80px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.2em;
  font-weight: 600;
}

.center {
  text-align: center;
}
</style>
