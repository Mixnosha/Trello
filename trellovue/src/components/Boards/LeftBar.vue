<template>
  <div style="background: #f16c6c; width: 100vw; height: 100vh;"  :style="{backgroundColor: select_board.background}">
    <div class="main">

      <!-- ================ BLOCK HEADER  ================ -->
      <div class="header">
        <div style="display: flex; align-items: center">
          <div class="icons">
            <img :src="wk.logo" alt="" style="width: 40px; border-radius: 6px">
          </div>
          <div class="title"> {{ wk.title }} </div>
        </div>
      </div>
      <hr style="color: rgba(255,255,255,0.93)">

      <!-- ================ BLOCK ICONS  ================ -->

      <div class="el__wk">
        <div class="el" style="" @click="this.$router.push({ name: 'home', params: { slug: wk.slug }})">
          <div class="el__icon" style="padding-right: 12px;"><img src="@/static/images/Boards/LeftBar/square-board.svg"
                                                                  style="width: 16px; border-radius: 2px" alt=""></div>
          <div class="el__lbl" style="font-size: 16px">
            Доски
          </div>
        </div>
        <div class="el" style="">
          <div class="el__icon" style="padding-right: 12px;"><img src="@/static/images/Boards/LeftBar/networking.svg"
                                                                  style="width: 16px; border-radius: 2px; fill: white"
                                                                  alt=""></div>
          <div class="el__lbl" style="font-size: 16px">Участники</div>
          <div class="add__user"
               style="display: flex; justify-content: center; width: 24px; color: #e1dada; border-radius: 4px; font-size: 20px; margin-left: 50%">
            +
          </div>
        </div>
        <div class="el" style="">
          <div class="el__icon" style="padding-right: 12px;"><img src="@/static/images/Boards/LeftBar/settings.svg"
                                                                  style="width: 16px; border-radius: 2px" alt=""></div>
          <div class="el__lbl" style="font-size: 16px"
               @click="this.$router.push({ name: 'account', params: { slug: wk.slug }})">Настройки
          </div>
        </div>
      </div>

      <!-- ================ BLOCK MY BOARDS  ================ -->

      <div class="my_boards" style="padding-bottom:10px;padding-top: 18px;">
        <div class="boards__title" style="display: flex; align-items: center">
          <div class="some__title"
               style="font-weight: 700; font-size: 14px; padding-left: 16px; padding-right: 12px; color:#e1dada">Мои
            доски
          </div>
          <div class="add__user"
               style="cursor:pointer; display: flex; justify-content: center; width: 24px; color: #e1dada; border-radius: 4px; font-size: 20px; margin-left: 54%"
               @click="display_createBr==='none'?display_createBr='block':display_createBr='none'"
          >
            +
          </div>
        </div>
        <div class="board"></div>
      </div>

      <div class="all_boards">
        <div class="one_board" v-for="b in boards" @click="go_router(b.slug, b.title)">
          <div class="bg_board" :style="{backgroundColor: b.background}"></div>
          <span style="padding-left: 10px; color: white">{{ b.title }}</span>
        </div>
      </div>

    </div>
  </div>


  <!-- ================ BLOCK CREATE BOARD ================ -->

  <div class="main_form_add_board" :style="{display: display_createBr}">
    <CreateBoard id="5"></CreateBoard>
  </div>

</template>

<script>
import CreateBoard from "@/components/HomeWK/CreateBoard";
import axios from "axios";
import Cookies from "js-cookie";

export default {
  components: {CreateBoard},
  data() {
    return {
      display_createBr: 'none',
      boards: null,
      wk_id: null,
      wk: 'undefined',
      select_board: 'null',
    }
  },
  methods: {
    go_router(slug, title) {
      this.$router.push({name: 'board', params: {slug: slug, title: title}})
    },
    async get_board(){
      const slug = this.$route.params.slug
      const res = await axios.get(`http://127.0.0.1:8000/api/v1/get_board_to_slug/${slug}`)
      this.wk_id = res.data.wk_id
      this.select_board = res.data
      console.log(this.select_board)
    },
    async get_wk(){
      const res = await axios.get(`http://127.0.0.1:8000/api/v1/workspace/${this.wk_id}`, {
        headers: {
          'Authorization': `Token ${Cookies.get('token')}`
        }

      })
      this.wk = res.data
    },
    async get_boards(id) {
      const res = await axios.get(`http://127.0.0.1:8000/api/v1/get_boards/${id}`, {
        headers: {
          'Authorization': `Token ${Cookies.get('token')}`
        }})
      this.boards = res.data
    }
  },
  async mounted() {
    await this.get_board()
    await this.get_boards(this.wk_id)
    await this.get_wk()
  }
}
</script>

<style scoped>
.main {
  background-color: rgba(28, 28, 28, 0.26);
  border-left: 1px solid rgba(255, 255, 255, 0.3);
  border-right: 1px solid rgba(255, 255, 255, 0.3);
  border-bottom: 1px solid rgba(255, 255, 255, 0.3);
  position: absolute;
  top: 44px;
  width: 300px;
  height: 100%;
}

.title {
  font-size: 16px;
  color: white;
  font-weight: 700;
}

.header {
  padding: 20px 20px 5px 20px;
}

/* ========== STYLE BLOCK ICONS ==========*/
.icons {
  padding-right: 10px;
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

.el__lbl {
  color: #f5f1f1;
}

/* ========== STYLE MY BOARDS ==========*/

.add__user:hover {
  background: rgba(211, 209, 209, 0.78);
}

/* ========== STYLE MY BOARDS ==========*/


.main_form_add_board {
  width: 395px;
  background: white;
  position: absolute;
  border-radius: 4px;
  left: 20.01%;
  top: 6.1%;

  padding: 14px;
  overflow: scroll;
}

.one_board {
  display: flex;
  width: 100%;
  height: 40px;
  align-items: center;
  transition: background-color 76ms;
}

.one_board:hover {
  background-color: rgba(255, 255, 255, 0.18);
}

.all_boards {

}

.bg_board {
  align-items: center;
  width: 36px;
  height: 24px;
  background: cornflowerblue;
  border-radius: 4px;
  margin-left: 12px;

}
</style>