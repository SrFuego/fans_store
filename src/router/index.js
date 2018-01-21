import Vue from 'vue'
import Router from 'vue-router'
import HomeView from '@/pages/home/HomeView'
import FaqView from '@/pages/faq/FaqView'
import AboutView from '@/pages/about/AboutView'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView
    },
    {
      path: '/preguntas-dudas',
      name: 'FaqView',
      component: FaqView
    },
    {
      path: '/nosotros',
      name: 'AboutView',
      component: AboutView
    }
  ]
})
