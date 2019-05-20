import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import './registerServiceWorker'
import '@fortawesome/fontawesome-free/css/all.css'
import 'bootstrap-css-only/css/bootstrap.min.css'
import 'mdbvue/build/css/mdb.css'

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
  iconfont: 'fa'
}).$mount('#app')
