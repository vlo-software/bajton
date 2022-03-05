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
  background: linear-gradient(107.13deg, #4e007d 0.37%, #0b001d 93.6%);
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
      background: #7d47f0;
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
        background: #8658e7;
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
