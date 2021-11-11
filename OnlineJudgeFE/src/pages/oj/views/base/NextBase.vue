<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import api from '@oj/api'

export default {
  name: 'app',
  components: {},
  mounted () {
    api.getUserInfo().then((res) => {
      if (res.data.data !== null) {
        window.location.href = '/home'
      }
    })
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,300;1,400;1,500;1,600;1,700;1,800&display=swap');
@import url('https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.0/font/bootstrap-icons.css');

body {
  margin: 0;
  padding: 0;
}

#app {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 100%;
}
</style>
