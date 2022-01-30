<template>
  <div>
    <!-- <img
      class="iphone"
      src="https://cdn.discordapp.com/attachments/702078695698858015/937131613085630494/unknown.png"
    />
    <img
      class="iphone2"
      src="https://cdn.discordapp.com/attachments/702078695698858015/937131613085630494/unknown.png"
    /> -->
    <el-form
      :model="ruleForm2"
      :rules="rules2"
      ref="ruleForm2"
      label-position="left"
      label-width="0px"
      class="demo-ruleForm login-container"
    >
      <marquee direction="right" behavior="alternate"
        ><h3 class="title">{{ $t('m.Welcome_to_Login') }}</h3></marquee
      >
      <el-form-item prop="account">
        <el-input
          type="text"
          v-model="ruleForm2.account"
          auto-complete="off"
          :placeholder="$t('m.username')"
          @keyup.enter.native="handleLogin"
        ></el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input
          type="password"
          v-model="ruleForm2.password"
          auto-complete="off"
          :placeholder="$t('m.password')"
          @keyup.enter.native="handleLogin"
        ></el-input>
      </el-form-item>
      <el-form-item style="width: 100%">
        <el-button
          type="primary"
          style="width: 100%"
          @click.native.prevent="handleLogin"
          :loading="logining"
          >{{ $t('m.GO') }}
        </el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import api from '../../api'

export default {
  data () {
    return {
      logining: false,
      ruleForm2: {
        account: '',
        password: ''
      },
      rules2: {
        account: [{ required: true, trigger: 'blur' }],
        password: [{ required: true, trigger: 'blur' }]
      },
      checked: true
    }
  },
  mounted () {
    // let audio = new window.Audio(
    //   'https://cdn.discordapp.com/attachments/875044086841753671/937130238490603630/Parabole_tancza-AGA_1HsP_C0.mp3'
    // )
    // document.documentElement.appendChild(audio)
    // window.onmousedown = () => {
    //   audio.play()
    //   window.onmousedown = undefined
    //   audio = null
    // }
  },
  methods: {
    handleLogin (ev) {
      this.$refs.ruleForm2.validate((valid) => {
        if (valid) {
          this.logining = true
          api.login(this.ruleForm2.account, this.ruleForm2.password).then(
            (data) => {
              this.logining = false
              // document.querySelector('audio').pause()
              this.$router.push({ name: 'dashboard' })
            },
            () => {
              this.logining = false
            }
          )
        } else {
          this.$error('Please check the error fields')
        }
      })
    }
  }
}
</script>

<style lang="less" scoped>
@keyframes shadow {
  from {
    box-shadow: 0 0 25px #ff0000;
  }
  50% {
    box-shadow: 0 0 25px #0000ff;
  }
  to {
    box-shadow: 0 0 25px #00ff00;
  }
}
@keyframes bajojajo {
  from {
    transform: rotate(-5deg);
    opacity: 0.7;
    filter: hue-rotate(0deg);
  }
  to {
    transform: rotate(5deg);
    opacity: 1;
    filter: hue-rotate(360deg);
  }
}
@keyframes sbin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
.iphone,
.iphone2 {
  position: fixed;
  scale: 0.5;
  animation: sbin 2s linear infinite;
}
.iphone {
  left: 40px;
}
.iphone2 {
  right: 40px;
}
.login-container {
  /*box-shadow: 0 0px 8px 0 rgba(0, 0, 0, 0.06), 0 1px 0px 0 rgba(0, 0, 0, 0.02);*/
  -webkit-border-radius: 5px;
  border-radius: 5px;
  -moz-border-radius: 5px;
  background-clip: padding-box;
  margin: 180px auto;
  width: 350px;
  padding: 35px 35px 15px 35px;
  background: #fff;
  border: 1px solid #eaeaea;
  animation: shadow 2s linear infinite alternate;
  //box-shadow: 0 0 25px #cac6c6;
  .title {
    margin: 0px auto 40px auto;
    color: #ff0077;
    animation: bajojajo 2s linear alternate infinite;
  }
  .remember {
    margin: 0px 0px 35px 0px;
  }
}
</style>
