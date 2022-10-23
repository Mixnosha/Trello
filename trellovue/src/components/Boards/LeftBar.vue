<template>
  <div style="background: #f16c6c; width: 100vw; height: 100vh; position: absolute; z-index: -99;"  :style="{backgroundColor: select_board.background}">
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
        <div class="one_board" style="" v-for="b in boards" @click="go_router(b.slug, b.title)"
             @mouseenter="boardsViewFunck(b.id, true)" @mouseleave="boardsViewFunck(b.id, false)">
          <div class="bg_board" :style="{backgroundColor: b.background}"></div>
          <span style="margin-right: auto; padding-left: 10px; color: white;">{{ b.title }}</span>
          <div  :id="b.id" @click.stop="console.log('d')" class="three_points">...</div>
          <div  :id="b.id + 'i'" class="navbar__icon">
            <svg class="icon" id="" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
                 viewBox="0 0 270.365 270.365" xml:space="preserve">
          <path style="" d="M269.884,103.996c-0.943-2.903-4.038-7.772-14.162-7.772h-73.543c-4.999,0-10.958-4.329-12.503-9.083
	l-22.726-69.945c-3.129-9.628-8.717-11.065-11.769-11.065c-3.052,0-8.64,1.438-11.769,11.066l-22.726,69.944
	c-1.545,4.754-7.504,9.083-12.502,9.083H14.642c-10.125,0-13.219,4.869-14.162,7.772c-0.943,2.902-1.302,8.661,6.89,14.612
	l59.497,43.226c4.044,2.939,6.32,9.944,4.775,14.698l-22.726,69.943c-1.867,5.745-1.578,10.358,0.858,13.711
	c1.868,2.572,4.827,4.047,8.118,4.047c3.14-0.001,6.432-1.283,10.065-3.923l59.497-43.227c1.929-1.401,4.745-2.205,7.729-2.205
	c2.982,0,5.798,0.804,7.727,2.205l59.497,43.229c3.634,2.639,6.927,3.922,10.066,3.922c3.29-0.001,6.248-1.476,8.116-4.048
	c2.437-3.352,2.725-7.966,0.858-13.709l-22.726-69.945c-1.545-4.753,0.731-11.759,4.775-14.697l59.499-43.226
	C271.187,112.656,270.828,106.899,269.884,103.996z M194.681,149.7c-9.277,6.74-13.769,20.563-10.225,31.468l20.228,62.258
	l-52.958-38.478c-4.499-3.27-10.374-5.069-16.543-5.069c-6.169,0-12.045,1.8-16.545,5.069L65.68,243.426l20.228-62.257
	c3.544-10.906-0.947-24.729-10.225-31.469l-52.959-38.477h65.462c11.466,0,23.224-8.543,26.767-19.448l20.229-62.259l20.229,62.259
	c3.544,10.905,15.302,19.448,26.769,19.448h65.462L194.681,149.7z"/>
</svg>
          </div>
        </div>
      </div>
      <div class="pop_menu">

      </div>
    </div>
  </div>


  <!-- ================ BLOCK CREATE BOARD ================ -->

  <div class="main_form_add_board" :style="{display: display_createBr}">
    <CreateBoard :id="this.wk_id"></CreateBoard>
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
      select_board: '',
      boardsView: false,
    }
  },
  methods: {
    go_router(slug, title) {
      this.$router.push({name: 'board', params: {slug: slug, title: title}}).then(() => { this.$router.go() })

    },
    boardsViewFunck(id, state){
      if (state){
        document.getElementById(id).style.display = 'flex'
        document.getElementById(id + 'i').style.display = 'block'
      }
      else {
        document.getElementById(id + 'i').style.display = 'none'
        document.getElementById(id).style.display = 'none'
      }
    },
    async get_board(){
      const slug = this.$route.params.slug
      const res = await axios.get(`http://127.0.0.1:8000/api/v1/get_board_to_slug/${slug}`)
      this.wk_id = res.data.wk_id
      this.select_board = res.data

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
  padding: 10px;
  box-sizing: border-box;
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

.three_points{
  cursor: pointer;
  display: none;
  align-items: center;
  justify-content: center;
  height: 28px;
  padding-bottom: 8px;
  padding-left: 6px;
  padding-right: 6px;
  border-radius: 4px;
  margin-right: 4px;
  font-size: 24px;
  transition: background-color 260ms;

}
.three_points:hover{
  background-color: rgba(200, 203, 208, 0.31);
}
.navbar__icon{
  width: 24px;
  display: none;
  margin-left: 6px;

}
.icon{
  width: 18px;
  transition: width 240ms;
  fill: #313030;
}
.navbar__icon:hover .icon{
  width: 20px;
}
</style>