<template>
  <div class="home-page">
    <div class="container">
      <div class="top">
        <a>
          <Logo class="logo" />
        </a>
      </div>
      <div class="main">
        <div class="content">
          <div class="title">{{ $t('m.LandingTitle') }}</div>
          <div class="text">{{ $t('m.LandingText') }}</div>
          <button @click="goRegister" class="btn-register">
            {{ $t('m.LandingBtnRegister') }}
          </button>
          <button @click="goLogin" class="btn-login">
            {{ $t('m.LandingBtnLogin') }}
          </button>
        </div>
        <div class="right">&lt;/&gt;</div>
      </div>
    </div>
    <section>
      <div
        class="section-subtitle"
        data-aos-duration="600"
        data-aos="fade-down"
      >
        Kto za tym stoi?
      </div>
      <div
        class="section-title"
        data-aos-delay="50"
        data-aos-duration="800"
        data-aos="fade"
      >
        Wspaniała szkoła
      </div>
      <div
        class="section-school-logo"
        data-aos-delay="100"
        data-aos-duration="1000"
        data-aos="fade"
      >
        <a href="https://www.vlo.gda.pl"><school-logo /></a>
      </div>
    </section>
  </div>
</template>

<script>
import Logo from '../components/Logo.vue'
import SchoolLogo from '../components/SchoolLogo.vue'

export default {
  name: 'home',
  components: {
    Logo,
    SchoolLogo
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
.home-page {
  overflow-x: hidden;
}
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
  background-size: cover;
  height: 100vh;
  padding-left: 3.5px;
  overflow-x: hidden;
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 130px 2fr 4fr 2fr;
  grid-template-areas:
    'top'
    '.'
    'main'
    '.';
  @media (max-height: 900px) {
    grid-template-rows: 130px 2fr 5fr 2fr;
  }
  @media (max-width: 560px) {
    grid-template-rows: 100px 1fr 7fr 1fr;
    width: 100%;
    padding-left: 0;
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
    &-login,
    &-register {
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
      background: #6647f0;
      &:hover {
        background: #4033b6;
      }
    }
    &-login {
      margin-left: 20px;
      background: #303182;
      &:hover {
        background: #202875;
      }
    }
  }

  @media (max-width: 1900px) {
    font-size: 8px;
    .title {
      line-height: 50px;
    }
    .text {
      line-height: 27px;
    }
  }

  @media (max-width: 1360px) {
    width: 70vw;
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
      &-register,
      &-login {
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

// Bottom section

section {
  background: #fff;
  min-height: 100vh;
  width: 100%;
}

.section-subtitle {
  text-align: center;
  font-size: 1.5em;
  font-weight: 600;
  font-family: 'Open Sans', sans-serif;
  color: #4a3082;
  padding: 90px 0px 10px 0px;
}

.section-title {
  text-align: center;
  font-size: 3em;
  font-weight: 700;
  font-family: 'Open Sans', sans-serif;
  color: #000;
  padding: 0px 0px 40px 0px;
  @media (max-width: 600px) {
    font-size: 2.3em;
  }
}

.section-school-logo {
  width: 100%;
  min-height: calc(100vh - 400px);
  display: flex;
  justify-content: center;
  align-items: center;
  svg {
    cursor: pointer;
  }
  @media (max-width: 600px) {
    min-height: calc(100vh - 600px);
    svg {
      max-width: calc(100% - 40px);
    }
  }
}
</style>
