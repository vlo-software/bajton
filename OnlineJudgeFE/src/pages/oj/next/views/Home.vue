<template>
  <div class="container">
    <div class="top">
      <Logo class="logo" />
    </div>
    <div class="main">
      <div class="content">
        <div class="title">{{ $t("m.LandingTitle") }}</div>
        <div class="text">{{ $t("m.LandingText") }}</div>
        <button @click="goRegister" class="btn-register">
          {{ $t("m.LandingBtnRegister") }}
        </button>
        <button @click="goLogin" class="btn-login">
          {{ $t("m.LandingBtnLogin") }}
        </button>
      </div>
      <div class="right">&lt;/&gt;</div>
    </div>
  </div>
</template>

<script>
import Logo from '../components/Logo.vue'

export default {
  name: 'home',
  components: {
    Logo
  },
  methods: {
    goRegister () {
      this.$router.push({ name: 'register' })
    },
    goLogin () {
      this.$router.push({ name: 'login' })
    }
  }
}
</script>

<style lang="less" scoped>
.container {
  height: 100vh;
  width: 100%;
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 130px 2fr 4fr 2fr;
  grid-template-areas:
    "top"
    "."
    "main"
    ".";
  @media (max-width: 560px) {
    grid-template-rows: 100px 1fr 7fr 1fr;
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
  .login-icon {
    position: absolute;
    top: 70px;
    right: 5vw;
    height: 40px;
    font-size: 32px;
    color: rgba(129, 75, 255, 0.5);
    cursor: pointer;
    @media (max-width: 560px) {
      font-size: 28px;
      top: 80px;
      right: 6vw;
    }
  }
}

.main {
  grid-area: main;
  display: flex;
  justify-content: center;
  align-items: center;
}

.content {
  width: 40vw;
  height: 100%;
  font-size: 10px;

  .title {
    font-weight: 800;
    font-size: 4.8em;
    line-height: 65px;
    color: #ffffff;
  }

  .text {
    margin-top: 30px;
    font-size: 2.4em;
    line-height: 33px;
    color: #cdbcff;
  }

  .btn {
    &-login, &-register {
      margin-top: 40px;
      height: 60px;
      width: 250px;
      box-sizing: border-box;
      border: none;
      border-radius: 5000px;
      color: #fff;
      font-weight: bold;
      font-size: 22px;
      line-height: 30px;
      text-align: center;
      transition: 0.2s ease;
      cursor: pointer;
    }
    &-register {
      background: #7d47f0;
      &:hover {
        background: #8658e7;
      }
    }
    &-login {
      margin-left: 20px;
      background: #4A3082;
      &:hover {
        background: #6943bd;
      }
    }
  }

  @media (max-width: 1360px) {
    width: 70vw;
    font-size: 8px;
    .title {
      line-height: 50px;
    }
  }

  @media (max-width: 760px) {
    width: calc(100vw - 80px);
    font-size: 7px;
    text-align: center;
    .title {
      line-height: 40px;
    }
    .text {
      margin-top: 20px;
      line-height: 25px;
    }
  }

  @media (max-width: 630px) {
    .btn {
      &-register, &-login {
        width: 100%;
      }
      &-login {
        margin-top: 20px;
        margin-left: 0px;
      }
    }
  }

  @media (max-width: 560px) {
    .btn {
      width: 100%;
    }
  }

  @media (max-width: 360px) {
    font-size: 6.5px;
  }

  @media (max-width: 320px) {
    font-size: 6px;
    .title {
      line-height: 30px;
    }
  }
}

.right {
  width: 40vw;
  height: 100%;
  font-family: Roboto;
  font-style: normal;
  font-weight: 200;
  font-size: 288px;
  text-align: center;
  color: #ffffff;
  user-select: none;
  @media (max-width: 1360px) {
    display: none;
  }
}
</style>