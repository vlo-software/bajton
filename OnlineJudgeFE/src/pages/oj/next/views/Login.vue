<template>
  <div ref="container" class="container">
    <div class="top">
      <a @click="goHome">
        <Logo class="logo" />
      </a>
    </div>
    <div class="main">
      <h1>{{ $t('m.LoginTitle') }}</h1>
      <div class="error" v-for="error in errors" v-bind:key="error">
        {{ error }}
      </div>
      <form @submit="handleLogin" :model="formLogin">
        <input
          v-model="formLogin.username"
          :placeholder="$t('m.LoginUsername')"
          type="text"
          @on-enter="handleLogin"
        />
        <input
          v-model="formLogin.password"
          :placeholder="$t('m.LoginPassword')"
          type="password"
          @on-enter="handleLogin"
        />
        <input
          v-if="tfaRequired"
          v-model="formLogin.tfa_code"
          :placeholder="$t('m.LoginTFA')"
          type="text"
        />
        <button v-if="!btnLoginLoading" type="submit">
          {{ $t('m.LoginBtn') }}
        </button>
        <button v-else type="submit">...</button>
      </form>
      <div class="no-account">
        <span>{{ $t('m.LoginNoAccount') }}</span>
        <a @click="goRegister">{{ $t('m.LoginRegister') }}</a>
      </div>
      <div class="forgot-password">
        <a @click="goResetPassword">{{ $t('m.LoginForgotPassword') }}</a>
      </div>
    </div>
  </div>
</template>

<script>
import FormMixin from '../mixins/form'
import Logo from '../components/Logo.vue'
import api from '@oj/api'
import { STORAGE_KEY } from '@/utils/constants'
import storage from '@/utils/storage'

export default {
  name: 'login',
  mixins: [FormMixin],
  components: {
    Logo
  },
  data () {
    return {
      tfaRequired: false,
      btnLoginLoading: false,
      errors: [],
      formLogin: {
        username: '',
        password: '',
        tfa_code: ''
      }
    }
  },
  mounted () {
    api.getUserInfo() // This is required so that we get the csrf token
  },
  methods: {
    async CheckRequiredTFA (username) {
      this.tfaRequired = (await api.tfaRequiredCheck(username)).data.data.result
    },
    async handleLogin (e) {
      e.preventDefault()

      this.btnLoginLoading = true

      this.errors = []

      if (this.formLogin.username === '') {
        this.errors.push(this.$t('m.LoginErrorMissingUsername'))
      } else {
        await this.CheckRequiredTFA(this.formLogin.username)
      }

      if (this.tfaRequired && this.formLogin.tfa_code === '') {
        this.errors.push(this.$t('m.LoginErrorMissingTFA'))
      }

      if (this.formLogin.password === '') {
        this.errors.push(this.$t('m.LoginErrorMissingPassword'))
      } else if (this.formLogin.password.length < 6) {
        this.errors.push(this.$t('m.LoginErrorShortPassword'))
      }

      if (this.errors.length !== 0) {
        this.btnLoginLoading = false
        return
      }

      this.btnLoginLoading = true
      let formData = Object.assign({}, this.formLogin)
      if (!this.tfaRequired) {
        delete formData['tfa_code']
      }
      api.login(formData).then(
        (res) => {
          storage.set(STORAGE_KEY.AUTHED, true)
          this.btnLoginLoading = false
          window.location.href = '/home'
        },
        (e) => {
          console.error(e)
          this.errors.push(e.data.data)
          this.btnLoginLoading = false
        }
      )
    },
    goRegister () {
      this.$router.push({ name: 'register' })
    },
    goResetPassword () {
      this.$router.push({ name: 'reset-password' })
    },
    goHome () {
      this.$router.push({ name: 'landing' })
    }
  },
  watch: {
    errors () {
      if (this.errors.length === 0) {
        this.$refs.container.style.setProperty(
          '--form-height',
          this.tfaRequired ? '580px' : '500px'
        )
      } else {
        this.$refs.container.style.setProperty(
          '--form-height',
          `${(this.tfaRequired ? 580 : 500) + 22 * this.errors.length}px`
        )
      }
    },
    tfaRequired () {
      // This watch will only trigger if tfa is required
      // since there is no way for it to be unrequired
      // there is no need to check the value of this.tfaRequired
      this.$refs.container.style.setProperty('--form-height', '580px')
    }
  }
}
</script>

<style lang="less" scoped>
.container {
  font-family: 'Open Sans', sans-serif;
  font-size: 14px;
  -webkit-font-smoothing: antialiased;
  width: 100%;
  min-height: 100vh;
  // background: linear-gradient(107.13deg, #4e007d 0.37%, #0b001d 93.6%);
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' version='1.1' xmlns:xlink='http://www.w3.org/1999/xlink' xmlns:svgjs='http://svgjs.com/svgjs' width='100%' height='100%' preserveAspectRatio='none' viewBox='0 0 3840 2160'%3e%3cg mask='url(%26quot%3b%23SvgjsMask1050%26quot%3b)' fill='none'%3e%3crect width='3840' height='2160' x='0' y='0' fill='rgba(21%2c 0%2c 75%2c 1)'%3e%3c/rect%3e%3cpath d='M0%2c1276.967C246.874%2c1244.727%2c487.172%2c1214.861%2c711.971%2c1107.849C962.424%2c988.625%2c1201.593%2c846.347%2c1369.08%2c625.238C1564.473%2c367.289%2c1789.483%2c69.626%2c1740.734%2c-250.28C1692%2c-570.085%2c1335.262%2c-728.975%2c1125.226%2c-975.014C913.196%2c-1223.389%2c815.28%2c-1617.672%2c500.186%2c-1703.477C184.795%2c-1789.363%2c-100.099%2c-1499.808%2c-408.962%2c-1392.795C-699.474%2c-1292.14%2c-1039.213%2c-1305.504%2c-1261.5%2c-1093.096C-1490.877%2c-873.914%2c-1634.511%2c-550.298%2c-1622.418%2c-233.268C-1610.899%2c68.717%2c-1335.177%2c277.784%2c-1198.919%2c547.528C-1069.686%2c803.364%2c-1087.291%2c1161.863%2c-842.427%2c1310.842C-597.373%2c1459.936%2c-284.431%2c1314.112%2c0%2c1276.967' fill='%2311003c'%3e%3c/path%3e%3cpath d='M3840 3597.775C4115.514 3615.091 4382.601 3514.627 4619.725 3373.276 4862.647 3228.469 5103.594 3047.425 5205.6810000000005 2783.685 5305.776 2525.091 5258.115 2230.244 5162.981 1969.784 5078.604 1738.774 4879.879 1583.295 4704.325 1411.058 4543.0689999999995 1252.848 4387.998 1090.987 4179.246 1004.635 3953.939 911.435 3709.212 852.392 3470.192 900.549 3220.066 950.943 3015.682 1111.743 2822.178 1278.0520000000001 2600.589 1468.499 2318.8940000000002 1646.27 2267.807 1933.953 2216.56 2222.537 2404.94 2496.161 2561.908 2743.685 2702.928 2966.06 2901.883 3132.765 3120.818 3279.069 3343.339 3427.77 3572.8940000000002 3580.987 3840 3597.775' fill='%2319005a'%3e%3c/path%3e%3c/g%3e%3cdefs%3e%3cmask id='SvgjsMask1050'%3e%3crect width='3840' height='2160' fill='white'%3e%3c/rect%3e%3c/mask%3e%3c/defs%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-attachment: fixed;
  --form-height: 500px;
  height: 100vh;
  width: 100%;
  display: grid;
  grid-template-columns: 3fr 2fr 3fr;
  grid-template-rows: 130px 1fr var(--form-height) 2fr;
  grid-template-areas:
    'top top top'
    '. . .'
    '. main .'
    '. . .';
  @media (max-width: 1600px) {
    grid-template-columns: 2fr 3fr 2fr;
  }
  @media (max-width: 900px) {
    grid-template-columns: 1fr 3fr 1fr;
  }
  @media (max-width: 675px) {
    grid-template-columns: 40px 1fr 40px;
  }
  @media (max-width: 450px) {
    grid-template-rows: 100px 1fr var(--form-height) 2fr;
    grid-template-columns: 0px 1fr 0px;
  }
}

.top {
  grid-area: top;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  a:hover {
    cursor: pointer;
  }
  @media (max-width: 560px) {
    .logo {
      transform: scale(0.7);
    }
  }
}

.main {
  grid-area: main;
  background: rgba(100, 11, 160, 0.2);
  border-radius: 10px;
  color: #cdbcff;
  h1 {
    text-align: center;
    padding-top: 20px;
  }
  .error {
    color: #f0475e;
    font-weight: bold;
  }
  form {
    margin: 40px auto 0 auto;
    display: flex;
    justify-content: center;
    flex-direction: column;
    input {
      background: rgba(205, 188, 255, 0.25);
      color: #fff;
      outline: none;
      height: 60px;
      width: calc(100% - 60px);
      box-sizing: border-box;
      padding: 10px 20px 10px 20px;
      margin: 0 30px 30px 30px;
      font-size: 18px;
      border: none;
      border-radius: 10px;
    }
    button {
      margin: 40px 30px 15px 30px;
      background: #6647f0;
      color: white;
      outline: none;
      height: 60px;
      font-weight: bold;
      font-size: 22px;
      line-height: 30px;
      border: none;
      border-radius: 10px;
      transition: 0.2s ease;
      cursor: pointer;
      &:hover {
        background: #4033b6;
      }
    }
  }

  .no-account,
  .forgot-password {
    display: flex;
    justify-content: center;
    a {
      cursor: pointer;
    }
  }

  .no-account {
    span {
      padding-right: 5px;
      user-select: none;
    }
    a {
      color: #fff;
    }
  }

  .forgot-password {
    padding-top: 10px;
    color: #dcd1fc;
  }

  @media (max-width: 450px) {
    border-radius: 0px;
  }

  input::placeholder {
    color: rgb(213, 146, 255) !important;
  }
}
</style>
