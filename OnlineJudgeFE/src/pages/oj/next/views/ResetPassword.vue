<template>
  <div ref="container" class="container">
    <div class="top">
      <a @click="goHome">
        <Logo class="logo" />
      </a>
    </div>
    <div class="main">
      <h1>{{ $t('m.ResetPasswordTitle') }}</h1>
      <div class="error" v-for="error in errors" v-bind:key="error">
        {{ error }}
      </div>
      <form @submit="handleReset" :model="formReset">
        <input
          v-model="formReset.email"
          :placeholder="$t('m.ResetPasswordEmail')"
          type="email"
          @on-enter="handleReset"
        />
        <div class="captcha">
          <input
            v-model="formReset.captcha"
            :placeholder="$t('m.ResetPasswordCaptcha')"
            type="text"
            @on-enter="handleReset"
          />
          <img alt="captcha" :src="captchaSrc" @click="getCaptchaSrc" />
        </div>
        <button v-if="!btnResetLoading" type="submit">
          {{ $t('m.ResetPasswordBtn') }}
        </button>
        <button v-else type="submit">...</button>
      </form>
    </div>
  </div>
</template>

<script>
import Logo from '../components/Logo.vue'
import FormMixin from '../mixins/form'
import api from '@oj/api'

export default {
  name: 'resetPassword',
  mixins: [FormMixin],
  components: {
    Logo
  },
  mounted () {
    this.getCaptchaSrc()
  },
  data () {
    return {
      btnResetLoading: false,
      errors: [],
      formReset: {
        email: '',
        captcha: ''
      }
    }
  },
  methods: {
    async handleReset (e) {
      e.preventDefault()

      this.btnResetLoading = true

      this.errors = []

      if (this.formReset.email === '') {
        this.errors.push(this.$t('m.ResetPasswordErrorMissingEmail'))
      }

      if (this.formReset.captcha === '') {
        this.errors.push(this.$t('m.ResetPasswordErrorMissingCaptcha'))
      } else if (
        this.formReset.captcha.length < 1 ||
        this.formReset.captcha.length > 10
      ) {
        this.errors.push(this.$t('m.ResetPasswordErrorCaptchaOutOfBounds'))
      }

      if (this.errors.length !== 0) {
        this.btnResetLoading = false
        return
      }

      this.btnResetLoading = true
      let formData = Object.assign({}, this.formReset)
      api.applyResetPassword(formData).then(
        (res) => {
          // TODO: Display message / go to another page
          window.alert('Check your email')
        },
        (e) => {
          window.alert(e.data.data)
          // TODO: Handle error
          this.btnLoginLoading = false
        }
      )
    },
    goHome () {
      this.$router.push({ name: 'landing' })
    }
  },
  watch: {
    errors () {
      if (this.errors.length === 0) {
        this.$refs.container.style.setProperty('--form-height', '460px')
      } else {
        this.$refs.container.style.setProperty(
          '--form-height',
          `${460 + 22 * this.errors.length}px`
        )
      }
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
  --form-height: 460px;
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
    .captcha {
      display: flex;
      justify-content: center;
      input {
        width: calc(100% - 180px);
        margin: 0 30px 30px 0px;
      }
      img {
        height: 60px;
        width: 90px;
        border-radius: 10px;
        cursor: pointer;
      }
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

  @media (max-width: 450px) {
    border-radius: 0px;
  }

  input::placeholder {
    color: rgb(213, 146, 255) !important;
  }
}
</style>
