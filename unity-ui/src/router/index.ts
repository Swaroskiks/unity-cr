import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '../views/LandingPage.vue'
import MainLayout from '../views/MainLayout.vue'
import TDsView from '../views/TDsView.vue'
import ProjectView from '../views/ProjectView.vue'
import AdminPage from '../views/AdminPage.vue'
import AuthorsPage from '../views/AuthorsPage.vue'

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
          path: 'tds',
          name: 'tds',
          component: TDsView
        },
        {
          path: 'project',
          name: 'project',
          component: ProjectView
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
