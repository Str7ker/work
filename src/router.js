import Vue from 'vue'
import Router from 'vue-router'
import Main from './views/Main.vue'
import Cargos from './views/Cargos'
import Company from './views/Company'
import Page from './views/Page'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/main',
      name: 'main',
      component: Main
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },
    {
      path: '/cargos',
      name: 'cargo',
      component: Cargos
    },
    {
      path: '/company',
      name: 'company',
      component: Company
    },
    {
      path: '/',
      name: 'page',
      component: Page
    },
  ]
})
