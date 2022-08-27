<template>
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
        <div v-for="wk in workspaces">
          <div class="workspace" :id="'workspace'+wk.id"  @click="menuVisible(wk.id)">
            <div class="workspace__icon" style="display: flex; align-items: center; justify-content: center">
              <img  src="@/static/images/wks.svg" style="width: 20px; border-radius: 4px">
            </div>
            <div class="workspace__title"
                 style="padding-left:5px; width: 100%">{{ wk.title }}
          </div>
          </div>
          <div :id='"open__menu"+wk.id' style="display: none">
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
  </div>
</template>

<script>
import axios from "axios";
import Cookies from "js-cookie";
import up_arrow from '@/static/images/up-arrow.svg'
import right_arrow from '@/static/images/arrow_right.svg'

export default {
  data() {
    return {
      menu_visible: false,
      workspaces: [],
    }
  },
  methods: {
    loadWK() {
      axios.get('http://192.168.100.6:8000/api/v1/workspace/', {
        headers: {
          'Authorization': `Token ${Cookies.get('token')}`
        }
      }).then(res => {
        for (let i = 0; i < res.data.length; i++) {
          this.workspaces.push(res.data[i])
        }
      })
    },
    menuVisible(el) {
      const id = "open__menu" + el
      const men_id = "workspace" + el
      let menu = document.getElementById(id)
      if (menu.style.display === 'none'){
        menu.style.display = 'block'
        document.getElementById(men_id).style.background=`#e4f0f6 url(${up_arrow}) no-repeat 95% 50%`
        document.getElementById(men_id).style.backgroundSize="12px"
      }else{
        menu.style.display = 'none'
        document.getElementById(men_id).style.background=`#e4f0f6 url(${right_arrow}) no-repeat 95% 50%`
        document.getElementById(men_id).style.backgroundSize="12px"
      }
    },
  },
  watch: {
  },
  mounted() {
    this.loadWK()
  }
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
  transition: background-color 64ms;
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
  width: 100%;
  display: flex;
  align-items: center;
  padding: 10px;
  margin-bottom: 8px;
  border-radius: 4px;
  background: white url("@/static/images/arrow_right.svg") no-repeat 95% 50% ;
  background-size: 12px;
  color: #0079bf;
  font-weight: 700;
  cursor: pointer;
}

.workspace:hover{
  background: rgba(150, 180, 231, 0.32) url("@/static/images/arrow_right.svg") no-repeat 95% 50% ;
  background-size: 12px;
}

.add {
  cursor: pointer;
}

.add:hover {
  background: rgba(150, 180, 231, 0.32);
}

.open__menu-label {
  margin-top: 8px;
  border-radius: 4px;
  padding: 8px;
  padding-left: 28px;
  display: flex;
  align-items: center;
  color: #42526e;
  font-size: 12px;
  transition: background-color 64ms;
}

.open__menu-label:hover {
  background: rgba(150, 180, 231, 0.32);
}

.open__lbl {
  padding-left: 8px;
}
</style>