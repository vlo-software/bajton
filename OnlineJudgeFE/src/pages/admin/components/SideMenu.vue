<template>
  <el-menu class="vertical_menu" :router="true" :default-active="currentPath">
    <div class="logo">
      <Logo @click="goHome" class="logo" />
    </div>
    <el-menu-item index="/"
      ><i class="el-icon-fa-dashboard"></i>{{ $t('m.Dashboard') }}</el-menu-item
    >
    <el-submenu v-if="isSuperAdmin" index="general">
      <template slot="title"
        ><i class="el-icon-menu"></i>{{ $t('m.General') }}</template
      >
      <el-menu-item index="/user">{{ $t('m.User') }}</el-menu-item>
      <el-menu-item index="/announcement">{{
        $t('m.Announcement')
      }}</el-menu-item>
      <el-menu-item index="/conf">{{ $t('m.System_Config') }}</el-menu-item>
      <el-menu-item index="/judge-server">{{
        $t('m.Judge_Server')
      }}</el-menu-item>
      <el-menu-item index="/prune-test-case">{{
        $t('m.Prune_Test_Case')
      }}</el-menu-item>
    </el-submenu>
    <el-submenu index="problem" v-if="hasProblemPermission">
      <template slot="title"
        ><i class="el-icon-fa-bars"></i>{{ $t('m.Problem') }}</template
      >
      <el-menu-item index="/problems">{{ $t('m.Problem_List') }}</el-menu-item>
      <el-menu-item index="/problem/create">{{
        $t('m.Create_Problem')
      }}</el-menu-item>
      <el-menu-item index="/problem/batch_ops">{{
        $t('m.Export_Import_Problem')
      }}</el-menu-item>
    </el-submenu>
    <el-submenu index="contest">
      <template slot="title"
        ><i class="el-icon-fa-trophy"></i>{{ $t('m.Contest') }}</template
      >
      <el-menu-item index="/contest">{{ $t('m.Contest_List') }}</el-menu-item>
      <el-menu-item index="/contest/create">{{
        $t('m.Create_Contest')
      }}</el-menu-item>
    </el-submenu>
  </el-menu>
</template>

<script>
import { mapGetters } from 'vuex'
import Logo from '../../oj/components/Logo.vue'

export default {
  name: 'SideMenu',
  components: { Logo },
  data () {
    return {
      currentPath: ''
    }
  },
  mounted () {
    this.currentPath = this.$route.path
  },
  computed: {
    ...mapGetters(['user', 'isSuperAdmin', 'hasProblemPermission'])
  }
}
</script>

<style scoped lang="less">
.el-menu {
  border-right: solid 1px var(--diff-tone-color);
}
.vertical_menu {
  overflow: auto;
  width: 270px;
  height: 100%;
  position: fixed !important;
  z-index: 100;
  top: 0;
  bottom: 0;
  left: 0;
  border: none;
  .logo {
    margin-top: 10px;
    transform: scale(0.75) translateX(-11%);
  }
}
</style>
