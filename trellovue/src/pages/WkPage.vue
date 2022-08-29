<template>
  <navbar></navbar>
  <div style="display: flex"><div class="wk__menu">
      <div class="wk__title-logo" style="display: flex; align-items: center; outline: 1px solid rgba(84, 83, 83, 0.32);">
        <div class="logo">
          <img :src="wk__logo" width="36" height="36" style="border-radius: 4px; margin-right: 4px; cursor: pointer;" alt="">
        </div>
        <div>
        <div class="lbl" style="font-size: 14px; font-weight: 700; cursor: pointer;">{{wk__title}}</div>
        <div style="font-size: 12px; color: #42526e">Бесплатно</div>
        </div>
      </div>
      <div class="el__wk" style="padding-top: 14px" >
        <div class="el" style="">
          <div class="el__icon" style="padding-right: 12px;"><img src="@/static/images/square-board.svg" style="width: 14px; border-radius: 2px" alt=""></div>
          <div class="el__lbl" style="font-size: 14px">Доски</div>
        </div>
        <div class="el" style="">
          <div class="el__icon" style="padding-right: 12px;"><img src="@/static/images/networking.svg" style="width: 14px; border-radius: 2px" alt=""></div>
          <div class="el__lbl" style="font-size: 14px">Участники</div>
          <div class="add__user" style="display: flex; justify-content: center; width: 24px; color: #6c6c6c; border-radius: 4px; font-size: 20px; margin-left: 50%">+</div>
        </div>
        <div class="el" style="">
          <div class="el__icon" style="padding-right: 12px;"><img src="@/static/images/settings.svg" style="width: 14px; border-radius: 2px" alt=""></div>
          <div class="el__lbl" style="font-size: 14px">Настройки</div>
        </div>
      </div>
      <div class="my_boards" style="padding-top: 18px;">
        <div class="boards__title" style="display: flex; align-items: center">
          <div class="some__title" style="font-weight: 700; font-size: 14px; padding-left: 16px">Мои доски</div>
          <div class="add__user" style="display: flex; justify-content: center; width: 24px; color: #6c6c6c; border-radius: 4px; font-size: 20px; margin-left: 54%">+</div>
        </div>
        <div class="board"></div>
      </div>
    </div>
    <div class="wk__main" style="height: 2000px"></div>
  </div>
</template>

<script>
import Navbar from "@/components/UI/Navbar";
import axios from "axios";
import Cookies from "js-cookie";
export default {
  components: {Navbar},
  data(){
    return {
      wk__title: '',
      wk__logo: '',
    }
  },
  methods: {
    async loadWk(){
        let id = Number(this.$route.params.slug.substring(this.$route.params.slug.length - 2))
        const res = await axios.get(`http://127.0.0.1:8000/api/v1/workspace/${id}`, {
          headers: {
            'Authorization': `Token ${Cookies.get('token')}`
          }
        })
      this.wk__title = res.data.title
      this.wk__logo = res.data.logo
    }
  },
  mounted() {
    this.loadWk()
}
}
</script>

<style scoped>
.wk__menu{
  z-index: 1;
  margin-top: 44px;
  background: white;
  width: 20%;
  min-height: 100vh;
  position: fixed;
  outline: 1px solid rgba(84, 83, 83, 0.32);
}
.wk__title-logo{
  padding: 16px;
}
.add__user:hover{
  background: rgba(175, 174, 174, 0.58);
}
.el{
  display: flex;
  width: 100%;
  padding-left: 16px;
  height: 36px;
  align-items: center;
  cursor: pointer;
  transition: background-color 64ms;
}
.el:hover{
  background: rgba(222, 222, 222, 0.58);
}
</style>