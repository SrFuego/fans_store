// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import _ from 'lodash'
// ui
import Ui from './ui'
// router
import router from './router'
// mixins
import Globals from './mixins'
// style
import './sass/main.scss'

Vue.config.productionTip = false

Vue.mixin(Globals)
Vue.use(Ui)
Vue.use(_)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
