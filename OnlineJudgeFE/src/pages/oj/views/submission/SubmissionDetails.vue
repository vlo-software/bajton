<template>
  <Grid style="width: 100%" justify="center">
    <Grid style="width: 80vw" direction="column" justify="around">
      <div id="status">
        <Alert :type="status.type" showIcon>
          <span class="title">{{
            $t('m.' + status.statusName.replace(/ /g, '_'))
          }}</span>
          <div slot="desc" class="content">
            <template v-if="isCE">
              <pre>{{ submission.statistic_info.err_info }}</pre>
            </template>
            <template v-else>
              <span
                >{{ $t('m.Time') }}:
                {{ submission.statistic_info.time_cost | submissionTime }}</span
              >
              <span
                >{{ $t('m.Memory') }}:
                {{
                  submission.statistic_info.memory_cost | submissionMemory
                }}</span
              >
              <span>{{ $t('m.Lang') }}: {{ submission.language }}</span>
              <span>{{ $t('m.Author') }}: {{ submission.username }}</span>
            </template>
          </div>
        </Alert>
      </div>

      <!--后台返info就显示出来， 权限控制放后台 -->
      <div v-if="submission.info && !isCE">
        <Panel style="margin-bottom: 10px">
          <div slot="title">
            <h4>{{ $t('m.Submission_Tests') }}</h4>
          </div>
          <Table
            stripe
            :loading="loading"
            :disabled-hover="true"
            :columns="columns"
            :data="submission.info.data"
          ></Table>
        </Panel>
        <Panel style="margin-bottom: 10px">
          <div slot="title">
            <h4>{{ $t('m.Submission_Outputs') }}</h4>
          </div>
          <div
            style="margin: 0px 35px; margin-bottom: 30px"
            v-for="item in submission.info.data.slice(0, 2)"
            v-bind:key="item['test_case']"
          >
            <h2 style="margin-bottom: 10px">{{ item['test_case'] }}.</h2>
            <h4>{{ $t('m.Submission_Output_Test') }}</h4>
            <Highlight
              :border-color="item.result === 0 ? '#10B060' : '#F00'"
              :code="item['test_output']"
            />
            <h4>{{ $t('m.Submission_Output_SubmissionOutput') }}</h4>
            <Highlight
              :border-color="item.result === 0 ? '#10B060' : '#F00'"
              :code="item['output']"
            />
          </div>
        </Panel>
      </div>
      <Panel style="margin-bottom: 10px">
        <div slot="title">
          <h4>{{ $t('m.Submission_Code') }}</h4>
        </div>
        <div style="margin: 0px 30px; margin-top: -20px">
          <Highlight
            :code="submission.code"
            :language="submission.language"
            :border-color="status.color"
          ></Highlight>
        </div>
      </Panel>
      <div v-if="submission.can_unshare">
        <div id="share-btn">
          <Button
            v-if="submission.shared"
            type="warning"
            size="large"
            @click="shareSubmission(false)"
          >
            {{ $t('m.UnShare') }}
          </Button>
          <Button
            v-else
            type="primary"
            size="large"
            @click="shareSubmission(true)"
          >
            {{ $t('m.Share') }}
          </Button>
        </div>
      </div>
    </Grid>
  </Grid>
</template>

<script>
import api from '@oj/api'
import { JUDGE_STATUS } from '@/utils/constants'
import utils from '@/utils/utils'
import Highlight from '@/pages/oj/components/Highlight'
import { Button, Table, Grid, Flex } from '@oj/bajton-ui'

export default {
  name: 'submissionDetails',
  components: {
    Highlight,
    Button,
    Table,
    Grid,
    Flex
  },
  data () {
    return {
      columns: [
        {
          title: this.$i18n.t('m.ID'),
          align: 'center',
          type: 'index'
        },
        {
          title: this.$i18n.t('m.Status'),
          align: 'center',
          render: (h, params) => {
            return h(
              'Tag',
              {
                props: {
                  color: JUDGE_STATUS[params.row.result].color
                }
              },
              this.$i18n.t(
                'm.' + JUDGE_STATUS[params.row.result].name.replace(/ /g, '_')
              )
            )
          }
        },
        {
          title: this.$i18n.t('m.Memory'),
          align: 'center',
          render: (h, params) => {
            return h('span', utils.submissionMemoryFormat(params.row.memory))
          }
        },
        {
          title: this.$i18n.t('m.Time'),
          align: 'center',
          render: (h, params) => {
            return h('span', utils.submissionTimeFormat(params.row.cpu_time))
          }
        }
      ],
      submission: {
        result: '0',
        code: '',
        info: {
          data: []
        },
        statistic_info: {
          time_cost: '',
          memory_cost: ''
        }
      },
      isConcat: false,
      loading: false
    }
  },
  mounted () {
    this.getSubmission()
  },
  methods: {
    getSubmission () {
      this.loading = true
      api.getSubmission(this.$route.params.id).then(
        (res) => {
          this.loading = false
          let data = res.data.data
          if (data.info && data.info.data && !this.isConcat) {
            // score exist means the submission is OI problem submission
            if (data.info.data[0].score !== undefined) {
              this.isConcat = true
              const scoreColumn = {
                title: this.$i18n.t('m.Score'),
                align: 'center',
                key: 'score'
              }
              this.columns.push(scoreColumn)
              this.loadingTable = false
            }
            if (this.isAdminRole) {
              this.isConcat = true
              const adminColumn = [
                {
                  title: this.$i18n.t('m.Real_Time'),
                  align: 'center',
                  render: (h, params) => {
                    return h(
                      'span',
                      utils.submissionTimeFormat(params.row.real_time)
                    )
                  }
                },
                {
                  title: this.$i18n.t('m.Signal'),
                  align: 'center',
                  key: 'signal'
                }
              ]
              this.columns = this.columns.concat(adminColumn)
            }
          }
          if (data.language === 'BrainFuck') {
            data.language = 'BrainF**k'
          }
          this.submission = data
        },
        () => {
          this.loading = false
        }
      )
    },
    shareSubmission (shared) {
      let data = { id: this.submission.id, shared: shared }
      api.updateSubmission(data).then(
        (res) => {
          this.getSubmission()
          this.$success(this.$i18n.t('m.Succeeded'))
        },
        () => {}
      )
    }
  },
  computed: {
    status () {
      return {
        type: JUDGE_STATUS[this.submission.result].type,
        statusName: JUDGE_STATUS[this.submission.result].name,
        color: JUDGE_STATUS[this.submission.result].color
      }
    },
    isCE () {
      return this.submission.result === -2
    },
    isAdminRole () {
      return this.$store.getters.isAdminRole
    }
  }
}
</script>

<style scoped lang="less">
#status {
  .title {
    font-size: 20px;
  }
  .content {
    margin-top: 10px;
    font-size: 14px;
    span {
      margin-right: 10px;
    }
    pre {
      white-space: pre-wrap;
      word-wrap: break-word;
      word-break: break-all;
    }
  }
}

.admin-info {
  margin: 5px 0;
  &-content {
    font-size: 16px;
    padding: 10px;
  }
}

#share-btn {
  float: right;
  margin-top: 5px;
  margin-right: 10px;
}

pre {
  border: none;
  background: none;
}
</style>
