<template>
  <div>
    <NavBar></NavBar>
    <div class="content-app">
      <router-view></router-view>
      <div class="footer">
        <p v-html="website.website_footer"></p>
        <p>
          Powered by
          <a
            style="color: var(--primary-color);"
            href="https://github.com/QingdaoU/OnlineJudge"
            >OnlineJudge</a
          >
          <span v-if="version">&nbsp; Version: {{ version }}</span>
        </p>
        <p>Customized by Zepsół Cyberniebezpieczeństwa V LO</p>
      </div>
    </div>
    <BackTop></BackTop>
  </div>
</template>

<script>
import { mapActions, mapGetters, mapState } from 'vuex'
import NavBar from '@oj/components/NavBar.vue'
import lightTheme from '@/styles/light.useable.less'
import darkTheme from '@/styles/dark.useable.less'

export default {
  name: 'base',
  components: {
    NavBar
  },
  data () {
    return {
      version: process.env.VERSION
    }
  },
  mounted () {
    this.getWebsiteConfig()
    const darkmode = window.localStorage.getItem('oj-darkmode')
    darkTheme.use() // Dark theme is the default
    if (darkmode !== null && darkmode !== 'true') {
      this.changeDarkMode(false)
    }
  },
  methods: {
    ...mapActions(['getWebsiteConfig', 'changeDomTitle', 'changeDarkMode'])
  },
  computed: {
    ...mapState(['website', 'darkMode']),
    ...mapGetters(['isAuthenticated'])
  },
  watch: {
    website () {
      this.changeDomTitle()
    },
    darkMode () {
      window.localStorage.setItem('oj-darkmode', this.darkMode)
      if (this.darkMode) {
        lightTheme.unuse()
        darkTheme.use()
      } else {
        darkTheme.unuse()
        lightTheme.use()
      }
    },
    $route () {
      this.changeDomTitle()
    },
    isAuthenticated () {
      // This handles logout
      if (!this.isAuthenticated) {
        window.location.href = '/next/'
      }
    }
  }
}
</script>

<style lang="less">
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}

a {
  text-decoration: none;
  background-color: transparent;
  &:active,
  &:hover {
    outline-width: 0;
  }
}

@media screen and (max-width: 1200px) {
  .content-app {
    margin-top: 160px;
    padding: 0 2%;
  }
}

@media screen and (min-width: 1200px) {
  .content-app {
    margin-top: 80px;
    padding: 0 2%;
  }
}

.footer {
  margin-top: 20px;
  margin-bottom: 10px;
  text-align: center;
  font-size: small;
}

.fadeInUp-enter-active {
  animation: fadeInUp 0.8s;
}
</style>
