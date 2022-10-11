import { createRouter, createWebHistory } from 'vue-router'
import Register from "@/pages/Register";
import Main from "@/pages/Main";
import WkPage from "@/pages/WkPage";
import Account from "@/pages/Account";
import HomeWK from "@/pages/HomeWK";
import Boards from "@/pages/Boards";

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
  },
  {
    path: '/w/:slug/account',
    name: 'account',
    component: Account,
  },
  {
    path: '/w/:slug/home',
    name: 'home',
    component: HomeWK,
  },
  {
    path: '/b/:slug/:slug',
    name: 'board',
    component: Boards
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
