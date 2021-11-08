<template>
<div ref="container" class="container">
    <div class="top">
        <Logo class="logo"/>
    </div>
    <div class="main">
      <h1>{{$t('m.RegisterTitle')}}</h1>
      <div class=error v-for="error in errors" v-bind:key="error">
        {{error}}
      </div>
      <form @submit="handleRegister" :model="formRegister">
        <input v-model="formRegister.email" :placeholder="$t('m.RegisterEmail')" type="email" @on-enter="handleRegister" />
        <input v-model="formRegister.username" :placeholder="$t('m.RegisterUsername')" type="text" @on-enter="handleRegister" />
        <input v-model="formRegister.password" :placeholder="$t('m.RegisterPassword')" type="password" @on-enter="handleRegister" />
        <div class="captcha">
          <input v-model="formRegister.captcha" :placeholder="$t('m.RegisterCaptcha')" type="text" @on-enter="handleRegister" />
          <img :src="captchaSrc" @click="getCaptchaSrc"/>
        </div>
        <button v-if="!btnRegisterLoading" type="submit">{{$t('m.RegisterBtn')}}</button>
        <button v-else type="submit">...</button>
      </form>
      <div class="account">
        <span>{{$t('m.RegisterAccountAlreadyExists')}}</span>
        <a @click="goLogin" >{{$t('m.RegisterLogin')}}</a>
      </div>
    </div>
</div>
</template>

<script>
  import Logo from '../components/Logo.vue'
  import FormMixin from '../mixins/form'
  import api from '@oj/api'

  export default {
    name: 'register',
    mixins: [FormMixin],
    components: {
      Logo
    },
    mounted () {
      this.getCaptchaSrc()
    },
    data () {
      return {
        btnRegisterLoading: false,
        errors: [],
        formRegister: {
          username: '',
          password: '',
          email: '',
          captcha: ''
        }
      }
    },
    methods: {
      async handleRegister (e) {
        e.preventDefault()

        this.errors = []

        // TODO: Email and username should be checked together

        if (this.formRegister.username === '') {
          this.errors.push(this.$t('m.RegisterErrorMissingUsername'))
        } else {
          const alreadyInDb = (await api.checkUsernameOrEmail(this.formRegister.username, undefined)).data.data.username
          if (alreadyInDb) {
            this.errors.push(this.$t('m.RegisterErrorUsernameTaken'))
          }
        }

        if (this.formRegister.password === '') {
          this.errors.push(this.$t('m.RegisterErrorMissingPassword'))
        } else if (this.formRegister.password.length < 6 || this.formRegister.password.length > 20) {
          this.errors.push(this.$t('m.RegisterErrorPasswordOutOfBounds'))
        }

        if (this.formRegister.email === '') {
          this.errors.push(this.$t('m.RegisterErrorMissingEmail'))
        } else {
          const alreadyInDb = (await api.checkUsernameOrEmail(undefined, this.formRegister.email)).data.data.email
          if (alreadyInDb) {
            this.errors.push(this.$t('m.RegisterErrorEmailAlreadyInUse'))
          }
        }

        if (this.formRegister.captcha === '') {
          this.errors.push(this.$t('m.RegisterErrorMissingCaptcha'))
        } else if (this.formRegister.captcha.length < 1 || this.formRegister.captcha.length > 10) {
          this.errors.push(this.$t('m.RegisterErrorCaptchaOutOfBounds'))
        }

        if (this.errors.length !== 0) {
          this.btnLoginLoading = false
          return
        }

        this.btnRegisterLoading = true

        let formData = Object.assign({}, this.formRegister)
        this.btnRegisterLoading = true
        api.register(formData).then(res => {
          // TODO: Display "thank you" message
          this.btnRegisterLoading = false
          this.$router.push({ name: 'login' })
        }, _ => {
          // TODO: Handle error
          this.getCaptchaSrc()
          this.formRegister.captcha = ''
          this.btnRegisterLoading = false
        })
      },
      goLogin () {
        this.$router.push({ name: 'login' })
      }
    },
    watch: {
      'errors' () {
        if (this.errors.length === 0) {
          this.$refs.container.style.setProperty('--form-height', '630px')
        } else {
          this.$refs.container.style.setProperty('--form-height', `${630 + 22 * this.errors.length}px`)
        }
      }
    }
  }
</script>

<style lang="less" scoped>
  .container {
    --form-height: 630px;
    height: 100vh;
    width: 100%;
    display: grid;
    grid-template-columns: 3fr 2fr 3fr;
    grid-template-rows: 130px 1fr var(--form-height) 2fr;
    grid-template-areas: 'top top top'
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
      grid-template-columns: 30px 1fr 30px;
    }
    @media (max-width: 450px) {
      grid-template-rows: 100px 1fr var(--form-height) 2fr;
      grid-template-columns: 0px 1fr 0px;
    }
    @media (max-height: 750px) {
      height: 120vh;
    }
  }

  .top {
    grid-area: top;
    display: flex;
    align-items: flex-end;
    justify-content: center;
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
    color: #CDBCFF;
    h1 {
      text-align: center;
      padding-top: 20px;
    }
    .error {
      color: #f0475e;
      padding-left: 50px;
      font-weight: bold;
    }
    form {
      margin: 40px auto 0 auto;
      display: flex;
      justify-content: center;
      flex-direction: column;
      input {
        background: #CDBCFF;
        color: #4E007D;
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
        margin: 0px 30px 15px 30px;
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

    .account {
      display: flex;
      justify-content: center;
      span {
        padding-right: 5px;
        user-select: none;
      }
      a {
        cursor: pointer;
        color: #fff;
      }
    }

    @media (max-width: 450px) {
      border-radius: 0px;
    }
  }
</style>