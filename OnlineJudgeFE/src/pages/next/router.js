import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from './views/Home.vue'
import Login from './views/Login.vue'
import Register from './views/Register.vue'
import ResetPassword from './views/ResetPassword.vue'
import ResetPasswordVerify from './views/ResetPasswordVerify.vue'
Vue.use(VueRouter)

export default new VueRouter({
  mode: 'history',
  base: '/next/',
  scrollBehavior: () => ({y: 0}),
  routes: [
    {
      name: 'landing',
      path: '/',
      component: Home
    },
    {
      name: 'login',
      path: '/login',
      component: Login
    },
    {
      name: 'register',
      path: '/register',
      component: Register
    },
    {
      name: 'reset-password',
      path: '/reset-password',
      component: ResetPassword
    },
    {
      name: 'reset-password-verify',
      path: '/reset-password-verify/:token',
      component: ResetPasswordVerify
    }
  ]
})
