<template>
  <navbar></navbar>
  <div class="right__navbar">
    <div class="right__lbl" style="">
      <div class="lbl">
        <img src="@/static/images/square-board.svg" style="width: 14px;">
        <div style="padding-left: 10px">Доски</div>
      </div>
      <div class="lbl">
        <img src="@/static/images/main.svg" style="width: 14px;">
        <div style="padding-left: 10px">Главная страница</div>

      </div>
    </div>
    <div class="right_workspaces">
      <div>
        <div class="add__workspaces">
          <div class="add__lbl" style="padding-right:90px; display: flex; align-items: center; justify-content: center">
            Рабочие пространства
          </div>
          <div class="add"
               style="border-radius: 5px;padding-right:10px; padding-left: 10px; font-weight: normal;color: #596477; font-size: 24px; display: flex; align-items: center; justify-content: center">
            +
          </div>
        </div>
        <div class="workspace" style="">
          <div class="workspace__icon" style="display: flex; align-items: center; justify-content: center">
            <img src="@/static/images/wks.svg" style="width: 20px; border-radius: 4px">
          </div>
          <div class="workspace__title" style="padding-left:5px; padding-right: 155px">Trello</div>
          <div class="workspace__arrow">
            <img src="@/static/images/arrow_right.svg" style="width: 12px; fill: black;">
          </div>
        </div>
        <div style="">
          <div class="open__menu-label">
            <img src="@/static/images/square-board.svg" alt="" width="12px">
            <div class="open__lbl">Доски</div>
          </div>
          <div class="open__menu-label">
            <img src="@/static/images/heart.svg" width="12px" alt="">
            <div class="open__lbl">Важнейшие события</div>
          </div>
          <div class="open__menu-label">
            <img src="@/static/images/menu.svg" width="12px" alt="">
            <div class="open__lbl">Представления</div>
          </div>
          <div class="open__menu-label">
            <img src="@/static/images/networking.svg" width="12px" alt="">
            <div class="open__lbl">Участники</div>
          </div>
          <div class="open__menu-label">
            <img src="@/static/images/settings.svg" width="12px" alt="">
            <div class="open__lbl">Найстройки</div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div>

  </div>
</template>
<script>
import MyButton from "@/components/UI/MyButton";
import {mapState} from "vuex";
import Navbar from "@/components/UI/Navbar";

export default {
  components: {MyButton, Navbar},
  data() {
    return {
      workspaces: '',
    }
  },
  methods: {
    addWorkspace() {
      console.log('sdfsdf')
    },
  },
  computed: {
    ...mapState({
      username: state => state.user.username,
    }),
  },
}
</script>

<style scoped>
.right__navbar {
  width: 258px;
  padding: 40px 0px;
  margin-left: 86px;

}

.lbl {
  font-weight: 700;
  display: flex;
  align-items: center;
  font-size: 15px;
  padding: 5px 0px 5px 5px;
  transition: background-color 32ms;
  border-radius: 3px;
  color: #293342;
}

.lbl:hover {
  background: rgba(150, 180, 231, 0.32);
}

.add__workspaces {
  display: flex;
  font-size: 12px;
  font-weight: 700;
  color: #42526e;
  padding: 10px 0px 4px 0px;
}

.workspace {
  display: flex;
  align-items: center;
  padding: 10px;
  border-radius: 4px;
  background-color: #e4f0f6;
  color: #0079bf;
  font-weight: 700;
  cursor: pointer;
}

.add {
  cursor: pointer;
}

.add:hover {
  background: rgba(150, 180, 231, 0.32);
}
.open__menu-label{
  margin-top: 8px;
  border-radius: 4px;
  padding: 3px;
  padding-left: 28px;
  display: flex;
  align-items: center;
  color: #42526e;
  font-size: 12px;
  transition: background-color 32ms;
}
.open__menu-label:hover{
  background: rgba(150, 180, 231, 0.32);
}
.open__lbl{
  padding-left: 8px;
}
</style>