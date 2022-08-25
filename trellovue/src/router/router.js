import { createRouter, createWebHistory } from 'vue-router'
import Register from "@/pages/Register";
import Main from "@/pages/Main";

const routes = [
  {
    path: '/register',
    name: 'register',
    component: Register
  },
  {
    path: '/',
    name: 'main',
    component: Main
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
