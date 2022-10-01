<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import AOS from 'aos'
import 'aos/dist/aos.css'

export default {
  name: 'app',
  components: {},
  mounted () {
    AOS.init()
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,300;1,400;1,500;1,600;1,700;1,800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap');
@import url('https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/font/bootstrap-icons.css');

body {
  margin: 0;
  padding: 0;
}

:root {
  scrollbar-width: thin;
  scrollbar-color: #4c007b #0b001d;
}

::-webkit-scrollbar {
  display: block;
  background: #0b001d;
  width: 7px;
}

::-webkit-scrollbar-thumb {
  background-color: #2c0c5f;
  border-radius: 10px;
}

#app {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 100%;
}
.error {
  text-align: center;
}
</style>
