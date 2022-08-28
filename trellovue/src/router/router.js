import { createRouter, createWebHistory } from 'vue-router'
import Register from "@/pages/Register";
import Main from "@/pages/Main";
import WkPage from "@/pages/WkPage";

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
    path: '/w/:slug',
    name: 'pageWk',
    component: WkPage,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
