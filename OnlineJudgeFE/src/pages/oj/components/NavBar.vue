<template>
  <div id="header">
    <Menu
      theme="light"
      mode="horizontal"
      @on-select="handleRoute"
      :active-name="activeMenu"
      class="oj-menu"
    >
      <div class="logo">
        <span>{{ website.website_name }}</span>
      </div>
      <Menu-item name="/home">
        <Icon type="home"></Icon>
        {{ $t('m.Home') }}
      </Menu-item>
      <Menu-item name="/problem">
        <Icon type="ios-keypad"></Icon>
        {{ $t('m.NavProblems') }}
      </Menu-item>
      <Menu-item name="/contest">
        <Icon type="trophy"></Icon>
        {{ $t('m.Contests') }}
      </Menu-item>
      <Menu-item name="/status">
        <Icon type="ios-pulse-strong"></Icon>
        {{ $t('m.NavStatus') }}
      </Menu-item>
      <Submenu name="rank">
        <template slot="title">
          <Icon type="podium"></Icon>
          {{ $t('m.Rank') }}
        </template>
        <Menu-item name="/acm-rank">
          {{ $t('m.ACM_Rank') }}
        </Menu-item>
        <Menu-item name="/oi-rank">
          {{ $t('m.OI_Rank') }}
        </Menu-item>
      </Submenu>
      <Submenu name="about">
        <template slot="title">
          <Icon type="information-circled"></Icon>
          {{ $t('m.About') }}
        </template>
        <Menu-item name="/about">
          {{ $t('m.Judger') }}
        </Menu-item>
        <Menu-item name="/FAQ">
          {{ $t('m.FAQ') }}
        </Menu-item>
      </Submenu>
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
      <div @click="toggleDarkmode" class="btn-darkmode">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          class="bi bi-moon-fill"
          viewBox="0 0 16 16"
        >
          <path
            d="M6 .278a.768.768 0 0 1 .08.858 7.208 7.208 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 0 1 .81.316.733.733 0 0 1-.031.893A8.349 8.349 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 0 1 6 .278z"
          />
        </svg>
      </div>
    </Menu>
    <Modal v-model="modalVisible" :width="400">
      <div slot="header" class="modal-title">
        {{ $t('m.Welcome_to') }} {{ website.website_name_shortcut }}
      </div>
      <component :is="modalStatus.mode" v-if="modalVisible"></component>
      <div slot="footer" style="display: none"></div>
    </Modal>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import login from '@oj/views/user/Login'
import register from '@oj/views/user/Register'
import { Button } from '@oj/bajton-ui'

export default {
  components: {
    login,
    register,
    Button
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
  height: auto;
  width: 100%;
  z-index: 1000;
  background-color: var(--background-color-full);
  box-shadow: 0 1px 5px 0 rgba(0, 0, 0, 0.1);
  .oj-menu {
    background: var(--background-color-full);
  }

  .logo {
    margin-left: 2%;
    margin-right: 2%;
    font-size: 20px;
    float: left;
    line-height: 60px;
  }

  .drop-menu {
    float: right;
    margin-right: 30px;
    position: absolute;
    right: 10px;
    &-title {
      font-size: 18px;
    }
  }
  .btn-menu {
    font-size: 16px;
    float: right;
    margin-right: 10px;
  }
  .btn-darkmode {
    float: right;
    height: 50px;
    margin-right: 20px;
    padding-top: 3px;
    transition: 0.2s ease;
    cursor: pointer;
    &:hover {
      color: var(--link-hover-color);
    }
  }
}

.modal {
  &-title {
    font-size: 18px;
    font-weight: 600;
  }
}
</style>
