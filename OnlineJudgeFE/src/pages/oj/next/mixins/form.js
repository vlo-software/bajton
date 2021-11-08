import api from '@oj/api'

export default {
  data () {
    return {
      captchaSrc: ''
    }
  },
  methods: {
    getCaptchaSrc () {
      api.getCaptcha().then(res => {
        this.captchaSrc = res.data.data
      })
    }
  }
}
