<template>
  <Grid style="width: 100%" justify="center">
    <div style="width: 80%">
      <Panel :padding="10">
        <div slot="title">{{ $t('m.OI_Ranklist') }}</div>
        <div class="echarts">
          <ECharts
            :style="
              darkMode
                ? 'filter: invert(0.75) saturate(10) hue-rotate(-180deg) saturate(2)'
                : ''
            "
            :options="options"
            ref="chart"
            auto-resize
          ></ECharts>
        </div>
        <Table :data="dataRank" :columns="columns" size="large"></Table>
      </Panel>
      <Pagination
        :total="total"
        :page-size.sync="limit"
        :current.sync="page"
        @on-change="getRankData"
        show-sizer
        @on-page-size-change="getRankData(1)"
      ></Pagination>
    </div>
  </Grid>
</template>

<script>
import { mapGetters } from 'vuex'
import api from '@oj/api'
import Pagination from '@oj/components/Pagination'
import utils from '@/utils/utils'
import { RULE_TYPE } from '@/utils/constants'
import { Table, Grid, Flex } from '@oj/bajton-ui'

export default {
  name: 'acm-rank',
  components: {
    Pagination,
    Table,
    Grid,
    Flex
  },
  computed: {
    ...mapGetters(['darkMode'])
  },
  data () {
    return {
      page: 1,
      limit: 30,
      total: 0,
      dataRank: [],
      columns: [
        {
          align: 'center',
          width: 60,
          render: (h, params) => {
            return h(
              'span',
              {},
              params.index + (this.page - 1) * this.limit + 1
            )
          }
        },
        {
          title: this.$i18n.t('m.User_User'),
          align: 'center',
          render: (h, params) => {
            return h(
              'a',
              {
                style: {
                  display: 'inline-block',
                  'max-width': '200px'
                },
                on: {
                  click: () => {
                    this.$router.push({
                      name: 'user-home',
                      query: { username: params.row.user.username }
                    })
                  }
                }
              },
              params.row.user.username
            )
          }
        },
        {
          title: this.$i18n.t('m.mood'),
          align: 'center',
          key: 'mood'
        },
        {
          title: this.$i18n.t('m.Score'),
          align: 'center',
          key: 'total_score'
        },
        {
          title: this.$i18n.t('m.AC'),
          align: 'center',
          key: 'accepted_number'
        },
        {
          title: this.$i18n.t('m.Total'),
          align: 'center',
          key: 'submission_number'
        },
        {
          title: this.$i18n.t('m.Rating'),
          align: 'center',
          render: (h, params) => {
            return h(
              'span',
              utils.getACRate(
                params.row.accepted_number,
                params.row.submission_number
              )
            )
          }
        }
      ],
      options: {
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: [this.$i18n.t('m.Score')]
        },
        grid: {
          x: '3%',
          x2: '3%'
        },
        toolbox: {
          show: true,
          feature: {
            dataView: { show: true, readOnly: true },
            magicType: { show: true, type: ['line', 'bar'] },
            saveAsImage: { show: true }
          },
          right: '10%'
        },
        calculable: true,
        xAxis: [
          {
            type: 'category',
            data: ['root'],
            boundaryGap: true,
            axisLabel: {
              interval: 0,
              showMinLabel: true,
              showMaxLabel: true,
              align: 'center',
              formatter: (value, index) => {
                return utils.breakLongWords(value, 14)
              }
            },
            axisTick: {
              alignWithLabel: true
            }
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: this.$i18n.t('m.Score'),
            type: 'bar',
            data: [0],
            barMaxWidth: '80',
            markPoint: {
              data: [{ type: 'max', name: 'max' }]
            }
          }
        ]
      }
    }
  },
  mounted () {
    this.getRankData(1)
  },
  methods: {
    getRankData (page) {
      let offset = (page - 1) * this.limit
      let bar = this.$refs.chart
      bar.showLoading({ maskColor: 'rgba(250, 250, 250, 0.8)' })
      api.getUserRank(offset, this.limit, RULE_TYPE.OI).then((res) => {
        if (page === 1) {
          this.changeCharts(res.data.data.results.slice(0, 10))
        }
        this.total = res.data.data.total
        this.dataRank = res.data.data.results
        bar.hideLoading()
      })
    },
    changeCharts (rankData) {
      let [usernames, scores] = [[], []]
      rankData.forEach((ele) => {
        usernames.push(ele.user.username)
        scores.push(ele.total_score)
      })
      this.options.xAxis[0].data = usernames
      this.options.series[0].data = scores
    }
  }
}
</script>

<style scoped lang="less">
.echarts {
  margin: 0 auto;
  width: 95%;
  height: 400px;
}
</style>
