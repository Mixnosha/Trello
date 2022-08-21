import { createRouter, createWebHistory } from 'vue-router'
import Register from "@/pages/Register";

const routes = [
  {
    path: '/register',
    name: 'register',
    component: Register
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
