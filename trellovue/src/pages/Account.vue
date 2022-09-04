<template>
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
              <img src="@/static/images/settings_page/lock.png" style="width: 12px;" alt="">
              <span style="padding-left: 6px; font-weight: 700">{{status.title}}</span>
                &nbsp;- Приватное рабочее пространство. Оно не индексируется и не видно никому кроме участников.
              </div>
            </div>
            <div>
              <button class="change__btn">Изменить</button>
            </div>
          </div>

          <div >
            <a class="delete__wk" href="">Удалить рабочее пространство ?</a>
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
import {mapState} from "vuex";

export default {
  components: {WkLeftMenu, Navbar, WkConst},

  data(){
    return {

    }
  },
  computed: {
    ...mapState({
      status: state => state.oneWk.wk.status
    })
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

.account__settings{
  padding: 40px 180px;
}
.wk__title{
  font-size: 18px;

  font-weight: 700;
}

.description_status{
  display: flex;
  margin-bottom: 40px;
}

.change__btn{
  border: none;
  outline: none;
  border-radius: 3px;
  color: #424242;
  background: rgba(215, 214, 214, 0.63);
  transition: background-color 64ms;
  margin-left: 24px;

}

.change__btn:hover{
  background: rgba(173, 172, 172, 0.7);
}

.delete__wk{
  color: #fc3b3b;
}

.delete__wk:hover{
  color: #6c6c6c;
}
</style>