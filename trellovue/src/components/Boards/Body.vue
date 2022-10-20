<template>
  <div class="main" @click="hidden">
    <BoardBar :title="select_board.title"></BoardBar>
    <div class="some_body">
      <!-- ===================== COLUMN ===============================-->
      <h1>{{ Columns }}</h1>
      <div class="column" v-for="clmn in columns" :id="clmn.id + 'main'">
        <div class="column__header">
          <div :id="clmn.id + 'd'" class="title" @dblclick="changeTitle(clmn.id)">{{ clmn.title }}</div>
          <input @keyup.enter="requestChangeTitle(clmn.id)" class='title_input' type="text"
                 :value="clmn.title" name="" :id="clmn.id">
          <div class="settings" @click="menuView(clmn.id + 'main', clmn.title)">...</div>
        </div>

        <div class="column__task" v-for="task in clmn.cards">
          <div class="task__title">{{ task.title }}</div>
          <div class="task__edit">
            <img src="@/static/images/Boards/Body/pencil.svg" class="pen_icon">
          </div>
        </div>

        <div class="add_task">
          <div class="add_task__icon">
            <img src="@/static/images/Boards/Body/plus.svg" class="pen_icon">

          </div>
          <div class="add_task_text">
            Добавить карточку
          </div>
        </div>
      </div>

      <!-- ====================================================================================  -->

      <div class="add_column" v-if="add_form_state === false"
           @click="add_form_state=true">
        <div class="add_column__icon">
          <img src="@/static/images/Boards/Body/plusWhite.svg" class="pen_icon">

        </div>
        <div class="add_clumn_text">
          Добавить еще одну колонку
        </div>
      </div>

      <div class="add_column-form" v-if="add_form_state">
        <input v-model="form_new_column.title" class="add_column_input" type="text"
               placeholder="Введите заголовок списка">
        <div style="display: flex; align-items: center">
          <div class="add_btn" @click="newColumn">Добавить список</div>
          <div class="add_column__icon"
               style="padding-left: 10px">
            <img src="@/static/images/Boards/Body/close.svg" class="close"
                 @click="add_form_state=false">
          </div>
        </div>
      </div>

      <!-- =============================== COLUMN MENU =================================  -->

      <div class="column_menu-main" id="menu" :style="{display: column_menu.display}">
        <div class="column_menu-header">
          <span class="column_menu-header-title">Действия со списком</span>
          <div  @click="column_menu.display = 'none'" class="wrapper_icon">
            <img class="column_menu-icons" src="@/static/images/Boards/Body/close.svg">
          </div>
        </div>
        <hr class="line">
        <div class="item">
          Добавить карточку...
        </div>
        <div class="item">
          Копировать список...
        </div>
        <div class="item">
          Переместить список...
        </div>
        <hr class="line">


        <div @click="column_menu.delete_state = true" class="item" v-if="column_menu.delete_state === false">
          Удалить список...
        </div>

        <div class="delete_column" v-else>
          <div style="color: #6c6c6c">
            Введите название списка
          </div>
          <input  v-model="column_menu.delete_column"
                  class="add_column_input"
                  :placeholder="column_menu.current_column.title"
                  style="width: 94%; height: 28px"
                  type="text">
          <div class="delete_close_btn">
            <div @click="delete_column" class="delete" :style="{background: column_menu.delete_btn_color, cursor: column_menu.delete_btn_cursor}">Удалить</div>
            <div class="close_btn" @click="column_menu.delete_state = false">Отменить</div>
          </div>
        </div>


      </div>



    </div>


  </div>
</template>
￼
<script>
import Cookies from "js-cookie";
import BoardBar from "@/components/Boards/BoardBar";
import axios from "axios";

export default {
  components: {BoardBar},
  data() {
    return {
      select_board: [],
      columns: [],
      add_form_state: false,
      form_new_column: {
        title: null,
        br_id: null
      },
      column_menu: {
        display: 'none',
        delete_state: false,
        delete_column: '',
        delete_btn_color:'#b7b0b0',
        delete_btn_cursor: '',
        current_column: ''
      },
      temp_parent_title: {
        parent: null,
        inpt: null
      }

    }

  },
  methods: {
    async get_board() {
      const slug = this.$route.params.slug
      const res = await axios.get(`http://127.0.0.1:8000/api/v1/get_board_to_slug/${slug}`)
      this.select_board = res.data
      this.form_new_column.br_id = res.data.id

    },
    async get_data() {
      const res = await axios.get(`http://127.0.0.1:8000/api/v1/column_list/${this.select_board.id}/`, {
        headers: {
          'Authorization': `Token ${Cookies.get('token')}`
        }
      })
      this.columns = res.data
    },

    changeTitle(id) {
      const el = document.getElementById(id)
      const parent = document.getElementById(id + 'd')
      if (this.temp_parent_title.parent !== null) {
        this.temp_parent_title.parent.style.display = 'block'
        this.temp_parent_title.inpt.style.display = 'none'
      } else {
        this.temp_parent_title.parent = parent
        this.temp_parent_title.inpt = el
      }
      el.style.display = 'block'
      parent.style.display = 'none'
      el.focus()
      this.temp_parent_title.parent = parent
      this.temp_parent_title.inpt = el
    },
    hidden(event) {
      if (event.target.className !== 'title') {
        this.temp_parent_title.parent.style.display = 'block'
        this.temp_parent_title.inpt.style.display = 'none'
        this.temp_parent_title.parent = null
        this.temp_parent_title.inpt = null
      }


    },
    menuView(id, title){
      this.column_menu.delete_state = false
      this.column_menu.delete_column = null
      const parent = document.getElementById(id)
      const position_parent = parent.getBoundingClientRect()
      const menu = document.getElementById('menu')
      menu.style.left = `${position_parent.left + 170}px`
      menu.style.top = `${position_parent.top + 10}px`
      this.column_menu.display = 'block'
      this.column_menu.current_column = {id: id, title: title}

    },
    requestChangeTitle(id) {
      axios.put(`http://127.0.0.1:8000/api/v1/column/${id}/`, {
            title: document.getElementById(id).value,
          },
          {
            headers: {
              'Authorization': `Token ${Cookies.get('token')}`
            }
          }).then(res => {
            for (let  i in this.columns){
              if (this.columns[i].id === id){
                this.columns[i].title = document.getElementById(id).value
              }
            }
        this.temp_parent_title.parent.style.display = 'block'
        this.temp_parent_title.inpt.style.display = 'none'
        this.temp_parent_title.parent = null
        this.temp_parent_title.inpt = null
      })

    },
    newColumn() {
      axios.post('http://127.0.0.1:8000/api/v1/column/', this.form_new_column, {
        headers: {
          'Authorization': `Token ${Cookies.get('token')}`
        }
      }).then(res => {
        this.columns.push(res.data)
        this.form_new_column.title = ''
      })

    },
    async delete_column(){
      if (this.column_menu.delete_btn_cursor === 'pointer'){
        const id =(parseInt(this.column_menu.current_column.id))
        await axios.delete(`http://127.0.0.1:8000/api/v1/column/${id}`, {
          headers: {
            'Authorization': `Token ${Cookies.get('token')}`
          }
        })
        for (let i in this.columns){
          if (this.columns[i].id === id){
            this.columns.splice(i, 1)
            this.column_menu.display = 'none'
            break
          }
        }
      }
    },
  },
  watch: {
    'column_menu.delete_column'(new_value){
      if (new_value === this.column_menu.current_column.title){
        this.column_menu.delete_btn_color = '#ce5f5f'
        this.column_menu.delete_btn_cursor = 'pointer'
      }
      else{
        this.column_menu.delete_btn_color = '#b7b0b0'
        this.column_menu.delete_btn_cursor = ''
      }
    }
  },
  async mounted() {
    await this.get_board()
    await this.get_data()

  }
}
</script>

<style scoped>
body{
  overflow-x: scroll;
}

input {
  all: unset;
}

.main {
  padding-left: 300px;
  padding-top: 45px;
}

.some_body {
  padding: 20px;
  display: flex;

}

/* ========== COLUMN ========= */

.column {
  max-width: 300px;
  height: 100%;
  background-color: #f1ecec;
  border-radius: 4px;
  padding: 10px;
  margin-right: 10px;

}

/* ========== COLUMN HEADER ========= */


.column__header {
  display: flex;
  padding-left: 10px;
  padding-bottom: 10px;
  align-items: center;
}

.title {
  -moz-user-select: none;
  -khtml-user-select: none;
  -webkit-user-select: none;
  user-select: none;

  font-weight: 700;
  font-size: 16px;
  display: block;
  cursor: pointer;
}

.title_input {
  border: 3px solid #3574e3;
  border-radius: 4px;
  padding-left: 5px;
  max-width: 180px;
  display: none;
}

.settings {
  margin-left: auto;
  font-weight: 700;
  color: #6e6b6b;
  padding-left: 8px;
  padding-right: 8px;
  border-radius: 4px;
  padding-bottom: 5px;
  cursor: pointer;
  transition: background-color 150ms;
}

.settings:hover {
  background-color: #cec9c9;

}


/* ========== COLUMN  TASK ========= */

.column__task {
  width: 100%;
  display: flex;
  margin-bottom: 10px;
  padding-bottom: 8px;
  padding-left: 10px;
  padding-right: 5px;
  padding-top: 8px;
  background-color: white;
  border-radius: 4px;
  box-shadow: 0px -5px 5px -5px rgba(34, 60, 80, 0.6) inset;
  transition: background-color 150ms;

}

.column__task:hover {
  background-color: #efeaea;

}

.task__title {

}

.task__edit {
  border-radius: 4px;
  width: 24px;
  display: flex;
  justify-content: center;
  cursor: pointer;
  transition: background-color 150ms;
  margin-left: auto;
}

.task__edit:hover {
  background-color: #cec9c9;

}

.pen_icon {
  width: 14px;
}


/* ========== COLUMN  ADD TASK ========= */

.add_task {
  display: flex;
  align-items: center;
  border-radius: 4px;
  padding: 5px 10px 5px 10px;
  color: #6e6b6b;
  transition: background-color 150ms;

}

.add_task:hover {
  background-color: #cec9c9;

}


.add_task__icon {
  padding-right: 10px;
}


/* ========== ADD COLUMN ========= */


.add_column {
  display: flex;
  padding: 10px 20px 10px 20px;
  height: 50px;
  align-items: center;
  border-radius: 4px;
  background-color: rgba(241, 237, 237, 0.27);
  transition: background-color 150ms;
}

.add_column:hover {
  background-color: rgba(241, 237, 237, 0.45);

}

.add_clumn_text {
  color: white;
}


.add_column__icon {
  padding-right: 10px;
}

/* ================== ADD NEW COLUMN FORM =====================*/

.add_column-form {
  width: 300px;
  max-height: 93px;
  background-color: #f1ecec;
  padding: 5px;
  border-radius: 4px;
}

.add_column_input {
  width: 270px;
  border: 3px solid #5380d0;
  border-radius: 3px;
  height: 36px;
  padding: 0px 0px 0px 15px;
  margin-bottom: 4px;
}

.add_column_input:focus {
  border-color: #5380d0;
}

.add_btn {
  background-color: #3069ce;
  color: white;
  border-radius: 4px;
  padding: 6px;
  transition: background-color 240ms;
}

.add_btn:hover {
  background-color: #1755c4;
}

.close {

  width: 24px;
}

.column_menu-main{
  display: none;
  position: absolute;
  background-color: #ffffff;
  border-radius: 4px;
  box-shadow: 0px -2px 2px -2px rgba(34, 60, 80, 0.6) inset;
  padding: 10px;

}

.column_menu-header{
  display: flex;
  width: 320px;
  padding: 5px 10px 10px 10px;
}

.column_menu-header-title{
  color: #a69a9a;
  margin: auto;
  font-size: 14px;
}

.column_menu-icons{
  cursor: pointer;
  width: 14px;
}

.line{
  color: #6c6c6c;
  padding: 0;
  margin: 0;
  margin-bottom: 5px;
}


.item{
  padding: 5px;
  margin-bottom: 5px;
  cursor: pointer;
  transition: background-color 240ms;
}

.item:hover{
  background-color: rgba(211, 208, 208, 0.57);
}

.wrapper_icon{
  padding: 2px;
  padding-left: 4px;
  padding-right: 4px;
  border-radius: 4px;
  transition: background-color 240ms;
}
.wrapper_icon:hover{
  background-color: rgba(108, 108, 108, 0.45);
}

/* ================== COLUMN MENU =====================*/

.delete_close_btn{
  display: flex;
  align-items: center;
  justify-content: center;
}

.delete{
  padding: 5px;
  color: white;
  background-color: #b7b0b0;
  border-radius: 4px;
  margin-right: 5px;
}

.close_btn{
  padding: 5px;
  color: white;
  background-color: #5da146;
  border-radius: 4px;
  transition: background-color 240ms;
  cursor: pointer;
}

.close_btn:hover{
  background-color: #71c554;
}




</style>