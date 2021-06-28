import { createRouter, createWebHistory } from 'vue-router'
import Posts from '../views/Posts.vue'
import Login from '../views/Login.vue'
import Logout from '../views/Logout.vue'
import Register from '../views/Register.vue'

const routes = [
  {
    path: '/',
    name: 'posts',
    component: Posts,
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/logout',
    name: 'logout',
    component: Logout
  },
  {
    path: '/register',
    name: 'register',
    component: Register
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
