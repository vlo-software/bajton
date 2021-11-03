import api from '../api'

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
