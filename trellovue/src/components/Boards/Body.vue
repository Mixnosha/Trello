<template>
  <div class="main">
    <BoardBar :title="select_board.title"></BoardBar>
    <div class="some_body">
      <!-- ===================== COLUMN ===============================-->
      <h1>{{Columns}}</h1>
      <div class="column" v-for="clmn in columns">
        <div class="column__header">
          <div class="title">{{ clmn.title }}</div>
          <div class="settings">...</div>
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

      <div class="add_column">
        <div class="add_column__icon">
          <img src="@/static/images/Boards/Body/plusWhite.svg" class="pen_icon">

        </div>
        <div class="add_clumn_text">
          Добавить еще одну колонку
        </div>
      </div>



      </div>


  </div>
</template>

<script>
import Cookies from "js-cookie";
import BoardBar from "@/components/Boards/BoardBar";
import axios from "axios";
export default {
  components: {BoardBar},
  data() {
    return {
      select_board: [],
      columns: []

    }

  },
  methods:{
    async get_board(){
      const slug = this.$route.params.slug
      const res = await axios.get(`http://127.0.0.1:8000/api/v1/get_board_to_slug/${slug}`)
      this.select_board = res.data

    },
    async get_data(){
        const res = await axios.get(`http://127.0.0.1:8000/api/v1/column_list/${this.select_board.id}/`, {
          headers: {
            'Authorization': `Token ${Cookies.get('token')}`
          }
        })
      this.columns = res.data
      },

  },
  async mounted() {
    await this.get_board()
    await this.get_data()
  }
}
</script>

<style scoped>
.main {
  padding-left: 300px;
  padding-top: 45px;
}

.some_body{
  padding: 20px;
  display: flex;

}

/* ========== COLUMN ========= */

.column{
  max-width: 300px;
  height: 100%;
  background-color: #f1ecec;
  border-radius: 4px;
  padding: 10px;
  margin-right: 10px;

}

/* ========== COLUMN HEADER ========= */


.column__header{
  display: flex;
  padding-left: 10px;
  padding-bottom: 10px;
  align-items: center;
}

.title{
  font-weight: 700;
  font-size: 16px;
  cursor: pointer;
}

.settings{
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

.settings:hover{
  background-color: #cec9c9;

}


/* ========== COLUMN  TASK ========= */

.column__task{
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

.column__task:hover{
  background-color: #efeaea;

}

.task__title{

}
.task__edit{
  border-radius: 4px;
  width: 24px;
  display: flex;
  justify-content: center;
  cursor: pointer;
  transition: background-color 150ms;
  margin-left: auto;
}

.task__edit:hover{
  background-color: #cec9c9;

}
.pen_icon{
  width: 14px;
}


/* ========== COLUMN  ADD TASK ========= */

.add_task{
  display: flex;
  align-items: center;
  border-radius: 4px;
  padding: 5px 10px 5px 10px;
  color: #6e6b6b;
  transition: background-color 150ms;

}

.add_task:hover{
  background-color: #cec9c9;

}


.add_task__icon{
  padding-right: 10px;
}


/* ========== ADD COLUMN ========= */


.add_column{
  display: flex;
  padding: 10px 20px 10px 20px;
  height: 50px;
  align-items: center;
  border-radius: 4px;
  background-color: rgba(241, 237, 237, 0.27);
  transition: background-color 150ms;
}

.add_column:hover{
  background-color: rgba(241, 237, 237, 0.45);

}

.add_clumn_text{
  color: white;
}


.add_column__icon{
  padding-right: 10px;
}


</style>