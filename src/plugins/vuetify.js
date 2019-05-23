import Vue from 'vue'
import Vuetify from 'vuetify'
import theme from './theme'
import 'vuetify/dist/vuetify.min.css'
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/src/stylus/app.styl'
import ru from 'vuetify/es5/locale/ru'
Vue.use(Vuetify, {
  iconfont: 'mdi',
  lang: {
    locales: { ru },
    current: 'ru'
  },
  theme
})
