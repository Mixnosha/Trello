<template>
  <div class="main">
    <BoardBar></BoardBar>
    <div class="some_body">


      <div class="column">
        <div class="column__header">
          <div class="title">Maksim</div>
          <div class="settings">...</div>
        </div>


        <div class="column__task">
          <div class="task__title">Maksim</div>
          <div class="task__edit">
            <img src="@/static/images/Boards/Body/pencil.svg" class="pen_icon">
          </div>
        </div>

        <div class="column__task">
          <div class="task__title">Maksim</div>
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
export default {
  components: {BoardBar},
  data() {
    return {
    }

  },
  methods:{

  },
  mounted() {
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
  padding-right: 180px;
}
.task__edit{
  border-radius: 4px;
  width: 24px;
  display: flex;
  justify-content: center;
  cursor: pointer;
  transition: background-color 150ms;
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
  padding: 5px 0px 5px 10px;
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