import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Posts from '../views/Posts.vue'

const routes = [
  {
    path: '/banana',
    name: 'Home',
    component: Home
  },
  {
    path: '/',
    name: 'posts',
    component: Posts
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
