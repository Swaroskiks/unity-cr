import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '../views/LandingPage.vue'
import MainLayout from '../views/MainLayout.vue'

import ProjectView from '../views/ProjectView.vue'
import AdminPage from '../views/AdminPage.vue'
import AuthorsPage from '../views/AuthorsPage.vue'
import DemoView from '../views/DemoView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'landing',
      component: LandingPage
    },
    {
      path: '/app',
      component: MainLayout,
      children: [

        {
          path: 'project',
          name: 'project',
          component: ProjectView
        },
        {
          path: 'demo',
          name: 'demo',
          component: DemoView
        },
        {
          path: 'authors',
          name: 'authors',
          component: AuthorsPage
        }
      ]
    },
    {
      path: '/admin',
      name: 'admin',
      component: AdminPage
    }
  ]
})

export default router
