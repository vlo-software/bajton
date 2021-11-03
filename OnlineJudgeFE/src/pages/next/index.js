import 'babel-polyfill'
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from '@/store'
import i18n from '@/i18n'
import VueAnalytics from 'vue-analytics'
import { GOOGLE_ANALYTICS_ID } from '@/utils/constants'

Vue.config.productionTip = false

Vue.use(VueAnalytics, {
  id: GOOGLE_ANALYTICS_ID,
  router
})

new Vue(Vue.util.extend({router, store, i18n}, App)).$mount('#app')
