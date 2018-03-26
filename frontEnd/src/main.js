import Vue from 'vue'
import App from './App'

import router from './router'
import store from './store'
import api from './api'

import ElementUI from 'element-ui'
// import 'element-ui/lib/theme-chalk/index.css'
import './element-variables.scss'
import './style/common.scss'
import SvgIcon from './svgIcons/template/SvgIcon.vue'

/* svg icon chunk */
(() => import(/* webpackChunkName: "svgIcon" */ './svgIcons'))()

/* register global component */
Vue.component('svg-icon', SvgIcon)

Vue.config.productionTip = false

Vue.prototype.$api = api
Vue.use(ElementUI)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
