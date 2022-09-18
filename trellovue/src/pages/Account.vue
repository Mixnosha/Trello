<template>
  <div @click="clickOut">
  <navbar></navbar>
  <div>
    <WkLeftMenu></WkLeftMenu>
    <div class="wk__main">
      <WkConst></WkConst>
      <hr style="width: 96%; margin: 0 auto">
      <div class="account__settings">
        <span style="font-size: 22px; font-weight: 700;">Настройки</span>
        <div class="status__wk" style="padding-top: 20px;">
          <div class="wk__title">Видимость рабочего пространства</div>
          <hr>
          <div class="description_status">
            <div style="display: flex; align-items: center">
              <div>

                <img v-if="status.title === 'Приватная'" src="@/static/images/settings_page/lock.png" style="width: 12px;" alt="">
                <img v-else :src="earth" style="width: 16px;" alt="">
                <span style="padding-left: 6px; font-weight: 700">{{ status.title }}</span>
                &nbsp;- {{ status.description }}
              </div>
            </div>
            <div>
              <button id="btn__change" class="change__btn"  @click="menu_vis === 'none'?menu_vis = 'block':menu_vis = 'none';">Изменить</button>
            </div>
          </div>

          <div>
            <a class="delete__wk" href="">Удалить рабочее пространство ?</a>
          </div>
        </div>

        <!-- ============== Change Form ============== -->
        <div id="nav" class="change__status" :style="{display: menu_vis}">

          <div class="change__title">
            <div class="title" style="padding-right: 40px;">Выбрать видимость рабочего ...</div>
            <img @click="menu_vis='none'" class="change__close" src="@/static/images/settings_page/close.svg" alt="">
          </div>
          <div style=" display: flex; justify-content: center;">
            <hr style="margin:0; width: 90%;">
          </div>

          <div class="change__text">

            <!-- ============== point ============== -->
            <div class="change__all-text" v-for="st in all_status" style="padding-bottom: 10px"  @click="change_status(st.title, st.description)">
              <div class="change__title-menu" >
                <img v-if="st.title === 'Приватная'" :src="img_lock" style="width: 12px;" alt="">
                <img v-else :src="earth" style="width: 16px;" alt="">
                <strong style="padding-left: 4px">{{ st.title }}</strong>
              </div>
              <div class="change__description">
                {{ st.description }}
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
  </div>
</template>

<script>
import Navbar from "@/components/UI/Navbar";
import WkLeftMenu from "@/components/UI/WkLeftMenu";
import WkConst from "@/components/UI/WkConst";
import {mapMutations, mapState} from "vuex";
import axios from "axios";
import Cookies from "js-cookie";
import img_lock from '@/static/images/settings_page/lock.png';
import earth from '@/static/images/settings_page/earth.png';

export default {
  components: {WkLeftMenu, Navbar, WkConst},

  data() {
    return {
      all_status: '',
      img_lock,
      earth,
      menu_vis: 'none',
    }
  },
  methods: {
    ...mapMutations({
      setWkStatus: 'oneWk/setWkStatus'
    }),
    getStatus(){
      axios.get('http://127.0.0.1:8000/api/v1/status/', {
        headers: {
          Authorization:  `Token ${Cookies.get('token')}`
        }
      }).then(res => {
        this.all_status = res.data
      })
    },
    clickOut(e){
      if (e.target.id !== 'btn__change'){
        let a = document.getElementById('nav')
        this.menu_vis = 'none'
      }
    },
    change_status(title, description){
      axios.put(`http://127.0.0.1:8000/api/v1/workspace/${this.id}/`, {
        status: {
          title: title,
          description: description
        }
      }, {
        headers: {
          'Authorization': `Token ${Cookies.get('token')}`
        }
      })
      this.setWkStatus({title: title, description: description})

    }
  },
  computed: {
    ...mapState({
      status: state => state.oneWk.wk.status,
      id: state => state.oneWk.id
    })
  },
  mounted() {
    this.getStatus()
  }
}

</script>

<style scoped>
.wk__main {
  position: relative;
  width: 1200px;
  height: 300px;
  left: 300px;
  top: 60px;
}

.account__settings {
  padding: 40px 180px;
}

.wk__title {
  font-size: 18px;

  font-weight: 700;
}

.description_status {
  display: flex;
  margin-bottom: 40px;
}

.change__btn {
  border: none;
  outline: none;
  border-radius: 3px;
  color: #424242;
  background: rgba(215, 214, 214, 0.63);
  transition: background-color 64ms;
  margin-left: 24px;

}

.change__btn:hover {
  background: rgba(173, 172, 172, 0.7);
}

.delete__wk {
  color: #fc3b3b;
}

.delete__wk:hover {
  color: #6c6c6c;
}

.change__status {
  position: absolute;
  background-color: #ffffff;
  left: 840px;
  border-radius: 4px;
  box-shadow: -5px 6px 10px rgba(155, 153, 153, 0.21);
  outline: 1px solid rgba(192, 191, 191, 0.62);
  bottom: -375px;

}

.change__title {
  display: flex;
  align-items: center;
  padding: 10px 10px 12px 40px;
  font-size: 16px;
  color: #6c6c6c;
}

.change__close {
  border-radius: 4px;
  transition: background-color 64ms;
}

.change__close:hover {
  background: rgba(194, 192, 192, 0.34);
}

.change__text {
  font-size: 14px;
  padding: 10px 18px 18px 18px;
}

.change__title-menu {
  display: flex;
  align-items: center;
  padding-bottom: 6px;
}
.change__all-text{
  cursor: pointer;
}
.change__all-text:hover{
  background-color: rgba(158, 190, 236, 0.12);
}

.change__description {
  color: #6c6c6c;

}
</style>