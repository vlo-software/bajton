<script>
export default {
  name: 'RenderTableHeader',
  functional: true,
  props: {
    render: Function,
    index: Number,
    column: { type: Object, default: null }
  },
  render: (h, ctx) => {
    const params = { index: ctx.props.index }
    if (ctx.props.column) params.column = ctx.props.column
    return ctx.props.render(h, params)
  }
}
</script>
