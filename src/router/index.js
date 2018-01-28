import Vue from 'vue'
import Router from 'vue-router'
import HomeView from '@/pages/home/HomeView'
import FaqPage from '@/pages/faq/FaqPage'
import AboutPage from '@/pages/about/AboutPage'
import ProductPage from '@/pages/products/ProductPage'

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
      name: 'FaqPage',
      component: FaqPage
    },
    {
      path: '/nosotros',
      name: 'AboutPage',
      component: AboutPage
    },
    {
      path: '/productos',
      name: 'ProductPage',
      component: ProductPage
    }
  ]
})
