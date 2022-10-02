<template>
  <div class="title">
    <span style="margin-left: 40%; margin-right: 24%">Создать доску</span>
    <div class="close">
      <img src="@/static/images/HomeWk/CreateBoard/close.svg" style="width: 15px">
    </div>
  </div>
  <hr style="color: grey">

  <div class="background_choices">
    <div class="test_bg" :style="{background: bg_color}"></div>
    <div class="some_choices">
      <span class="color">Фон</span>
    </div>
    <div style="display: flex; padding-bottom: 20px">
      <div v-for="color in colors" class="colors" :id="color.substring(1)" :style="{background: color}" @click="setColor($event, color)">
        <img :src="tick" style="width: 10px" v-if="color === colors[0]">
      </div>
    </div>

    <div style="padding-bottom: 20px">
      <div style="display: flex">
        <span class="text">Заголовок доски</span>
        <span style="color: red">*</span>
      </div>
      <input v-model="boards_data.title" type="text" class="inpt">
      <span v-if="boards_data.prow">👋 Укажите название доски.</span>
    </div>

    <div>
      <span class="text">Видимость</span><br>
      <div class="select_boards" @click="open_select_boards">
        {{ boards_select.current_choice_title }}</div>
      <div :style="{display: boards_select.display}" class="options_boards">
        <div class="option_el"
             v-for="st in boards_data.status"
             :id="st.id" @click="selected_el(st.id, st.title)">
          <div style="padding: 40px">
            <img src="@/static/images/settings_page/lock.svg" style="width: 24px" alt="">
          </div>
          <div>
            <span style="font-size: 15px; font-weight: 700">{{ st.title }}</span><br>
            <span style="font-size: 14px">{{ st.description }}</span>
          </div>
        </div>


      </div>
    </div>

  </div>
</template>

<script>
import tick from "@/static/images/HomeWk/CreateBoard/tick.svg"
import axios from "axios";
import Cookies from "js-cookie";
export default {
  props: {},
  data() {
    return {
      tick: tick,
      bg_color: "#7490ee",
      data: '7490ee',
      boards_select:{
        display: 'none',
        current_choice_id: '3',
        current_choice_title: 'Выберите видимость вашей доски',
      },
      boards_data:{
        title: '',
        prow: true,
        status: '',
      },
      colors: [
        "#7490ee",
        "#f8cc5f",
        "#358a03",
        "#fa4251",
        "#8019b4",
        "#d617f3",
        "#afee74",
        "#27b8cb",

      ],
    }
  },
  methods:{
    setColor(event, color){
      let el = document.getElementById(event.target.id)
      let del_el = document.getElementById(this.data)
      while (del_el.firstChild) {
        del_el.removeChild(del_el.firstChild);
      }
      this.data = event.target.id
      el.innerHTML = `<img src="${tick}" style="width: 10px">`
      this.bg_color = color
    },
    selected_el(id, title){
      let old_el = document.getElementById(this.boards_select.current_choice_id)
      old_el.style.background = 'white'
      old_el.children[1].style.color = 'black'
      this.boards_select.current_choice_id = id
      let el = document.getElementById(id)
      el.style.background = '#15469d'
      el.children[1].style.color = 'white'
      this.boards_select.current_choice_title = title
      this.boards_select.display = 'none'



    },
    open_select_boards(){
      if (this.boards_data.status === '')
      {
        axios.get('http://127.0.0.1:8000/api/v1/status/', {
          headers: {
            Authorization:  `Token ${Cookies.get('token')}`
          }
        }).then(res => {
          this.boards_data.status = res.data
        })
      }
      if (this.boards_select.display === 'none'){
        this.boards_select.display = 'block'
      }
      else{
        this.boards_select.display = 'none'
      }
    },
  },

  watch:{
    'boards_data.title'(newValue){
      if (newValue === ''){
        this.boards_data.prow = true
      }
      else{this.boards_data.prow = false}

    }
  },
}
</script>

<style scoped>
.title {
  display: flex;
  align-items: center;
}

.close {
  align-items: center;
  justify-content: center;
  display: flex;
  height: 20px;
  border-radius: 3px;
  width: 5%;
  transition: background-color 64ms;
}

.close:hover {
  background: rgba(162, 162, 162, 0.59);
}

.test_bg {
  width: 60%;
  margin-right: auto;
  margin-left: auto;
  height: 150px;
  border-radius: 5px;
  margin-bottom: 20px;
  box-shadow: -3px 3px 7px rgba(155, 153, 153, 0.99);
}

.colors{
  display: flex;
  width: 40%;
  height: 36px;
  border-radius: 3px;
  margin-right: 5px;
  justify-content:center;
}
.text{
  color: #6c6c6c;
  font-weight: 700
}

input{
  all: unset;
}
.inpt{
  border: 3px solid #f67272;
  border-radius: 4px;
  width: 100%;
  height: 36px;
  margin-bottom: 5px;
}

.inpt:focus{
  border-color: #5380d0;
}
.select_boards{
  width: 100%;
  cursor: pointer;
  padding: 5px 0px 5px 10px;
  border-radius: 4px;
  border: 3px solid #5380d0;
}

.options_boards{
  position: absolute;
  top: 84%;
  border: 1px solid rgba(161, 160, 160, 0.58);
  border-radius: 4px;
  width: 370px;
  padding: 2px 2px 0px 0px;
}

.option_el{
  width: 100%;
  background: white;
  display: flex;
  padding: 5px;
  transition: background-color 64ms;
  cursor: pointer;
}
.option_el:hover{
  background: rgb(201, 206, 206);
}
</style>