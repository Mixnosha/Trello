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
              <img src="@/static/images/settings_page/lock.png" style="width: 12px;" alt="">
              <span style="padding-left: 6px; font-weight: 700">{{status.title}}</span>
              <div>
                &nbsp;- Приватное рабочее пространство. Оно  не видно никому кроме участников.
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
  align-items: center;
  margin-bottom: 40px;
}

.change__btn{
  border: none;
  outline: none;
  padding: 4px;
  border-radius: 3px;
  margin-left: 86%;
}

.delete__wk{
  color: #fc3b3b;
}
</style>