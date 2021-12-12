<template>
  <Flex justify="around" style="width: 100%">
    <div>
      <panel
        shadow
        v-for="(contest, index) of contests"
        :key="index"
        class="contest"
      >
        <div slot="title">
          <Button
            type="text"
            class="contest-title"
            @click="() => goContest(index)"
            >{{ contest.title }}</Button
          >
        </div>
        <div class="contest-content">
          <div class="contest-content-tags">
            <Button type="info" shape="circle" size="small" icon="calendar">
              {{ contest.start_time | localtime('YYYY-M-D HH:mm') }}
            </Button>
            <Button type="success" shape="circle" size="small" icon="clock">
              {{ getDuration(contest.start_time, contest.end_time) }}
            </Button>
            <Button type="warning" shape="circle" size="small" icon="trophy">
              {{ contest.rule_type }}
            </Button>
          </div>
          <div class="contest-content-description">
            <blockquote v-html="contest.description"></blockquote>
          </div>
        </div>
      </panel>
      <Announcements class="announcement"></Announcements>
    </div>
  </Flex>
</template>

<script>
import Announcements from './Announcements.vue'
import api from '@oj/api'
import time from '@/utils/time'
import { CONTEST_STATUS } from '@/utils/constants'
import { Button, Grid, Flex } from '@oj/bajton-ui'

export default {
  name: 'home',
  components: {
    Announcements,
    Button,
    Grid,
    Flex
  },
  data () {
    return {
      contests: []
    }
  },
  mounted () {
    let params = { status: CONTEST_STATUS.NOT_START }
    api.getContestList(0, 5, params).then((res) => {
      this.contests = res.data.data.results
    })
  },
  methods: {
    getDuration (startTime, endTime) {
      return time.duration(startTime, endTime)
    },
    goContest (index) {
      this.$router.push({
        name: 'contest-details',
        params: { contestID: this.contests[index].id }
      })
    }
  }
}
</script>

<style lang="less" scoped>
.contest {
  margin-bottom: 10px;
  &-title {
    font-style: italic;
    font-size: 21px;
  }
  &-content {
    padding: 0 70px 40px 70px;
    &-description {
      margin-top: 25px;
    }
  }
}

.announcement {
  margin-top: 20px;
}
</style>
