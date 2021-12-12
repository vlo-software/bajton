<template>
  <div class="container">
    <Card :padding="0">
      <div class="flex-container">
        <div class="menu">
          <div class="avatar-editor">
            <div class="avatar-container">
              <img class="avatar" :src="profile.avatar" />
              <div class="avatar-mask">
                <a @click.stop="goRoute({ name: 'profile-setting' })">
                  <div class="mask-content">
                    <Icon type="camera" size="30"></Icon>
                    <p class="text">change avatar</p>
                  </div>
                </a>
              </div>
            </div>
          </div>

          <Button
            @click="() => goRoute('/setting/profile')"
            :type="activeName === '/setting/profile' ? 'primary' : 'ghost'"
            class="menu-item"
          >
            {{ $t('m.Profile') }}
          </Button>
          <Button
            @click="() => goRoute('/setting/account')"
            :type="activeName === '/setting/account' ? 'primary' : 'ghost'"
            class="menu-item"
          >
            {{ $t('m.Account') }}
          </Button>
          <Button
            @click="() => goRoute('/setting/security')"
            :type="activeName === '/setting/security' ? 'primary' : 'ghost'"
            class="menu-item"
          >
            {{ $t('m.Security') }}
          </Button>
          <!-- </Menu> -->
        </div>
        <div class="panel">
          <router-view></router-view>
        </div>
      </div>
    </Card>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
import { Card, Button } from '@oj/bajton-ui'

export default {
  name: 'profile',
  components: {
    Card,
    Button
  },
  methods: {
    goRoute (routePath) {
      this.$router.push(routePath)
    }
  },
  computed: {
    ...mapGetters(['profile']),
    activeName () {
      return this.$route.path
    }
  }
}
</script>

<style lang="less" scoped>
@avatar-radius: 50%;

.menu-item {
  width: calc(100% - 30px);
  margin: 5px 15px;
}

.container {
  width: 90%;
  min-width: 800px;
  margin: auto;
}

.flex-container {
  .menu {
    flex: 1 0 250px;
    max-width: 250px;
    .avatar-editor {
      padding: 10% 22%;
      margin-bottom: 10px;
      .avatar-container {
        &:hover {
          .avatar-mask {
            opacity: 0.5;
          }
        }
        position: relative;
        .avatar {
          width: 100%;
          height: auto;
          max-width: 100%;
          display: block;
          border-radius: @avatar-radius;
          box-shadow: 0px 0px 1px 0px;
        }
        .avatar-mask {
          transition: opacity 0.2s ease-in;
          z-index: 1;
          border-radius: @avatar-radius;
          position: absolute;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background: black;
          opacity: 0;
          .mask-content {
            position: absolute;
            top: 50%;
            left: 50%;
            z-index: 3;
            color: var(--background-color-full);
            font-size: 16px;
            text-align: center;
            transform: translate(-50%, -50%);
            .text {
              white-space: nowrap;
            }
          }
        }
      }
    }
  }

  .panel {
    flex: auto;
  }
}

.ivu-menu-vertical.ivu-menu-light:after {
  /*取消默认的伪元素*/
  width: 0;
}
</style>

<style lang="less">
.setting-main {
  position: relative;
  margin: 10px 40px;
  padding-bottom: 20px;
  .setting-content {
    margin-left: 20px;
  }
  .mini-container {
    width: 500px;
  }
}
</style>
