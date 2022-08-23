import { createRouter, createWebHistory } from 'vue-router'
import Register from "@/pages/Register";
import Main from "@/pages/Main";
import Login from "@/pages/Login";

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
  {
    path: '/login',
    name: 'login',
    component: Login
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
