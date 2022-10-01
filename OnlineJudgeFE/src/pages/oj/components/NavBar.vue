<template>
  <div id="header">
    <div class="content">
      <div class="left">
        <a @click="() => handleRoute('/home')">
          <logo
            :style="darkMode ? '' : 'filter: invert(100)'"
            class="logo"
          />
        </a>
        <i
          @click="() => handleRoute('/home')"
          :class="`icon bi bi-house ${activeMenu === '/home' ? 'active' : ''}`"
        />
        <i
          @click="() => handleRoute('/problem')"
          :class="`icon bi bi-clipboard ${
            activeMenu === '/problem' ? 'active' : ''
          }`"
        />
        <i
          @click="() => handleRoute('/contest')"
          :class="`icon bi bi-trophy ${
            activeMenu === '/contest' ? 'active' : ''
          }`"
        />
        <i
          @click="() => handleRoute('/status')"
          :class="`icon bi bi-activity ${
            activeMenu === '/status' ? 'active' : ''
          }`"
        />
        <Dropdown margin="8" @on-click="handleRoute">
          <i
            :class="`icon bi bi-bar-chart ${
              activeMenu === '/acm-rank' || activeMenu === '/oi-rank'
                ? 'active'
                : ''
            }`"
          />
          <Dropdown-menu slot="list">
            <Dropdown-item name="/acm-rank">
              {{ $t('m.ACM_Rank') }}
            </Dropdown-item>
            <Dropdown-item name="/oi-rank">
              {{ $t('m.OI_Rank') }}
            </Dropdown-item>
          </Dropdown-menu>
        </Dropdown>
        <Dropdown margin="8" @on-click="handleRoute">
          <i
            :class="`icon bi bi-info-circle ${
              activeMenu === '/about' || activeMenu.toLowerCase() === '/faq'
                ? 'active'
                : ''
            }`"
          />
          <Dropdown-menu slot="list">
            <Dropdown-item name="/about">
              {{ $t('m.Judger') }}
            </Dropdown-item>
            <Dropdown-item name="/FAQ">
              {{ $t('m.FAQ') }}
            </Dropdown-item>
          </Dropdown-menu>
        </Dropdown>
      </div>
      <div class="right">
        <template>
          <Dropdown
            class="drop-menu"
            @on-click="handleRoute"
            placement="bottom"
            trigger="click"
          >
            <Button type="text" class="drop-menu-title"
              >{{ user.username }}
              <Icon type="arrow-down-b"></Icon>
            </Button>
            <Dropdown-menu slot="list">
              <Dropdown-item name="/user-home">{{
                $t('m.MyHome')
              }}</Dropdown-item>
              <Dropdown-item name="/status?myself=1">{{
                $t('m.MySubmissions')
              }}</Dropdown-item>
              <Dropdown-item name="/setting/profile">{{
                $t('m.Settings')
              }}</Dropdown-item>
              <Dropdown-item v-if="isAdminRole" name="/admin">{{
                $t('m.Management')
              }}</Dropdown-item>
              <Dropdown-item divided name="/logout">{{
                $t('m.Logout')
              }}</Dropdown-item>
            </Dropdown-menu>
          </Dropdown>
        </template>
        <i v-if="!darkMode" @click="toggleDarkmode" class="icon bi bi-moon"></i>
        <i
          v-else
          @click="toggleDarkmode"
          class="icon bi bi-brightness-high"
        ></i>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import login from '@oj/views/user/Login'
import register from '@oj/views/user/Register'
import { Button, Dropdown, DropdownMenu, DropdownItem } from '@oj/bajton-ui'
import Logo from './Logo'

export default {
  components: {
    login,
    register,
    Button,
    Dropdown,
    DropdownMenu,
    DropdownItem,
    Logo
  },
  mounted () {
    this.getProfile()
  },
  methods: {
    ...mapActions(['getProfile', 'changeModalStatus', 'changeDarkMode']),
    handleRoute (route) {
      if (route && route.indexOf('admin') < 0) {
        this.$router.push(route)
      } else {
        window.open('/admin/')
      }
    },
    handleBtnClick (mode) {
      this.changeModalStatus({
        visible: true,
        mode: mode
      })
    },
    toggleDarkmode () {
      this.changeDarkMode(!this.darkMode)
    }
  },
  computed: {
    ...mapGetters([
      'website',
      'darkMode',
      'modalStatus',
      'user',
      'isAdminRole'
    ]),
    // 跟随路由变化
    activeMenu () {
      return '/' + this.$route.path.split('/')[1]
    },
    modalVisible: {
      get () {
        return this.modalStatus.visible
      },
      set (value) {
        this.changeModalStatus({ visible: value })
      }
    }
  }
}
</script>

<style lang="less" scoped>
#header {
  min-width: 300px;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 60px;
  z-index: 1000;
  backdrop-filter: blur(20px);
  background-color: var(--background-color-full);

  .content {
    position: absolute;
    left: 2vw;
    right: 2vw;
    top: 0px;
    bottom: 0px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .content .left,
  .right {
    display: flex;
    align-items: center;
    height: 100%;
  }

  .content .left {
    justify-content: flex-start;
  }

  .content .right {
    justify-content: flex-end;
  }

  .logo {
    height: 30px;
    width: 180px;
    margin-right: 10px;
  }

  .icon {
    font-size: 22px;
    line-height: 22px;
    padding: 9px 15px;
    border-radius: 8px;
    cursor: pointer;
    transition: background 0.2s ease;
  }

  .active {
    background: var(--navbar-active);
  }

  @media only screen and (max-width: 600px) {
    .logo {
      display: none;
    }
    .icon {
      font-size: 18px;
      line-height: 22px;
      padding: 9px 11px;
    }
  }
}
</style>
