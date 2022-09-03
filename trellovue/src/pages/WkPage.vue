<template>
  <navbar></navbar>
  <main  style="">
    <div class="wk__menu">
      <div class="wk__title-logo"
           style="display: flex; align-items: center; outline: 1px solid rgba(84, 83, 83, 0.32);">
        <div class="logo">
          <img :src="wk.logo" width="36" height="36" style="border-radius: 4px; margin-right: 4px; cursor: pointer;"
               alt="">
        </div>
        <div>
          <div class="lbl" style="font-size: 14px; font-weight: 700; cursor: pointer;">{{ wk.title }}</div>
          <div style="font-size: 12px; color: #42526e">Бесплатно</div>
        </div>
      </div>
      <div class="el__wk" style="padding-top: 14px">
        <div class="el" style="">
          <div class="el__icon" style="padding-right: 12px;"><img src="@/static/images/square-board.svg"
                                                                  style="width: 14px; border-radius: 2px" alt=""></div>
          <div class="el__lbl" style="font-size: 14px">Доски</div>
        </div>
        <div class="el" style="">
          <div class="el__icon" style="padding-right: 12px;"><img src="@/static/images/networking.svg"
                                                                  style="width: 14px; border-radius: 2px" alt=""></div>
          <div class="el__lbl" style="font-size: 14px">Участники</div>
          <div class="add__user"
               style="display: flex; justify-content: center; width: 24px; color: #6c6c6c; border-radius: 4px; font-size: 20px; margin-left: 50%">
            +
          </div>
        </div>
        <div class="el" style="">
          <div class="el__icon" style="padding-right: 12px;"><img src="@/static/images/settings.svg"
                                                                  style="width: 14px; border-radius: 2px" alt=""></div>
          <div class="el__lbl" style="font-size: 14px">Настройки</div>
        </div>
      </div>
      <div class="my_boards" style="padding-top: 18px;">
        <div class="boards__title" style="display: flex; align-items: center">
          <div class="some__title" style="font-weight: 700; font-size: 14px; padding-left: 16px">Мои доски</div>
          <div class="add__user"
               style="display: flex; justify-content: center; width: 24px; color: #6c6c6c; border-radius: 4px; font-size: 20px; margin-left: 54%">
            +
          </div>
        </div>
        <div class="board"></div>
      </div>
    </div>
    <div class="wk__main">
      <div class="const__wk">
        <div class="top_block_elements" style="">
          <div class="right_el" style="display: flex">
            <img :src="wk.logo" alt="" style="width: 70px; height: 70px; border-radius: 6px">
            <!-- ================= Block title ======================-->
            <div style="padding-left: 12px;" :class="[readMenuVis?'menuNone':'']">
              <div style="display: flex; align-items: center; padding-bottom: 2px">
                <span
                    style="font-size: 20px; font-weight: 700; padding-right: 5px; height: auto;">{{ wk.title }}</span>
                <div class="update__inf" @click="readMenuVis === false?readMenuVis=true:readMenuVis=false">
                  <img style="width: 14px" src="@/static/images/settings_page/pencil.svg" alt="">
                </div>
              </div>
              <div style="display: flex; align-items: center; padding-bottom: 2px">
                <img src="@/static/images/settings_page/lock.svg" style="width:14px; margin-right: 4px; ">
                <span style="color: #6c6c6c; font-size: 12px">{{ wk.status }}</span>
              </div>
              <div style="color: #6c6c6c; font-size: 12px">
                {{ wk.description }}
              </div>
            </div>
            <!-- ================= Read menu ======================-->
            <div :class="[readMenuVis?'read_menu':'menuNone']">
              <div class="el__form">
                <div style="display: flex">
                  <span class="title__form">Название</span>
                  <span style="color: #f55e5e">*</span>
                </div>
                <input type="text" class="input__form" v-model="wk.title">
              </div>

              <div class="el__form">
                <div style="display: flex">
                  <span class="title__form">Короткое название</span>
                  <span style="color: #f55e5e">*</span>
                </div>
                <input type="text" class="input__form" v-model="wk.slug">
              </div>

              <div class="el__form">
                <div style="display: flex">
                  <span class="title__form">Сайт (опционально)</span>
                  <span style="color: #ffff">*</span>
                </div>
                <input type="text" class="input__form" v-model="wk.web_site">
              </div>

              <div class="el__form">
                <div style="display: flex">
                  <span class="title__form">Описание (опционально)</span>
                  <span style="color: #f55e5e">*</span>
                </div>
                <textarea  type="text" class="area" v-model="wk.description"></textarea>
              </div>
              <button class="my_btn" @click="readInfoWk" style="margin-right: 4px;">Сохранить</button>
              <button class="btn_close" @click="readMenuVis=false">Отмена</button>
            </div>
          </div>
        </div>
        <button class="my_btn"><img src="@/static/images/settings_page/add_member.svg" style="width: 17px;padding-right: 2px">
          Пригласите пользователей в рабочее пространство</button>

      </div>

      <hr style="width: 96%; margin: 0 auto">
      <div class="boards__wk">

      </div>
    </div>
  </main>
</template>

<script>
import Navbar from "@/components/UI/Navbar";
import axios from "axios";
import Cookies from "js-cookie";

export default {
  components: {Navbar},
  data() {
    return {
      wk: {
        title: '',
        logo: '',
        status: '',
        description: '',
        slug: '',
        web_site: '',
      },
      id: '',
      readMenuVis: false,
    }
  },
  methods: {
    async loadWk() {
      this.id = Number(this.$route.params.slug.substring(this.$route.params.slug.length - 2))
      const res = await axios.get(`http://127.0.0.1:8000/api/v1/workspace/${this.id}`, {
        headers: {
          'Authorization': `Token ${Cookies.get('token')}`
        }
      })
      this.wk.title = res.data.title
      this.wk.logo = res.data.logo
      this.wk.status = res.data.status.title
      this.wk.description = res.data.description
      this.wk.slug = res.data.slug
      this.wk.web_site = res.data.web_site
    },
    async readInfoWk() {
      const res = await axios.put(`http://127.0.0.1:8000/api/v1/workspace/${this.id}/`, {
        title: this.wk.title,
        slug: this.wk.slug,
        web_site: this.wk.web_site,
        description: this.wk.description,

      }, {
        headers: {
          'Authorization': `Token ${Cookies.get('token')}`
        }
      })
      if (res.status === 200){
        this.readMenuVis = false
        this.$router.push({ name: 'pageWk', params: { slug: this.wk.title + this.id }})
      }
      setTimeout(() => { location.reload()}, 200);

    }
  },
  watch: {
  },
  mounted() {
    this.loadWk()
  }
}
</script>

<style scoped>
.wk__menu {
  margin-top: 44px;
  background: white;
  width: 20%;
  min-height: 100vh;
  position: fixed;
  outline: 1px solid rgba(84, 83, 83, 0.32);
}

.wk__title-logo {
  padding: 16px;
}

.add__user:hover {
  background: rgba(175, 174, 174, 0.58);
}

.el {
  display: flex;
  width: 100%;
  padding-left: 16px;
  height: 36px;
  align-items: center;
  cursor: pointer;
  transition: background-color 64ms;
}

.el:hover {
  background: rgba(222, 222, 222, 0.58);
}


.const__wk {
  width: 100%;
  padding-left: 120px;
  padding-top: 40px;
  display: flex;
  padding-bottom: 40px;
}

.wk__main {
  position: relative;
  width: 1200px;
  height: 300px;
  left: 300px;
  top: 60px;

}

.update__inf {
  border-radius: 4px;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background-color 64ms;
  cursor: pointer;
}

.update__inf:hover {
  background: rgba(108, 108, 108, 0.32);
}

.my_btn{
  background: #0079bf;
  border: none;
  box-sizing: border-box;
  border-radius: 3px;
  color: white;
  padding: 2px 6px;
  height: 32px;
  margin-left: auto;
  transition: background-color 64ms;
}

.my_btn:hover{
  background: #01629a;
}

.read_menu{
  padding: 5px 20px;
}
.el__form{
  padding-bottom: 20px;
}
.input__form{
  outline: 3px solid #cbcbcb;
  border-radius: 2px;
  border: none;
  height: 34px;
  padding-left: 12px;
}

.title__form{
  color: #8d8787;
  font-weight: 700;
  font-size: 12px;
}

.area{
  resize: none;
  width: 100%;
  height: 62px;
  outline: 3px solid #cbcbcb;
  border-radius: 2px;
  border: none;
  padding-left: 12px;
  padding-top: 8px;
}

.btn_close{
  background: rgba(198, 200, 201, 0.43);
  border: none;
  box-sizing: border-box;
  border-radius: 3px;
  color: #3f3f3f;
  padding: 2px 6px;
  height: 32px;
  margin-left: auto;
  transition: background-color 64ms;
}

.btn_close:hover{
  background: rgba(138, 139, 140, 0.43);
}

.menuNone{
  display: none;
}
</style>