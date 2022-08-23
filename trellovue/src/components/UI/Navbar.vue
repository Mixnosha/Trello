<template>
  <div class="navbar">

    <div class="navbar__btns">
      <div style="display: flex; align-items: center">
        <strong><div style="width: auto; height: 20px" @click="$router.push('/')">Trello</div></strong>
      <div style="width: auto; height: 20px"><a class="btn" @click="$router.push('/posts')">Рабочие пространства<img style="width: 13px; margin-left: 5px" src="@/static/images/arrow.svg"></a></div>
      <div style="width: auto; height: 20px"><a class="btn" @click="$router.push('/store')">Недавние</a></div>
        <div style="width: auto; height: 20px"><a class="btn" @click="$router.push('/about')">В избранном</a></div>
        <div style="width: auto; height: 20px"><a class="btn" @click="$router.push('/post_api')">Создать</a></div>
        <div style="width: auto; height: 20px"><input type="text" placeholder="Поиск" class="myInput"></div>
        <div style="width: auto; height: 20px"><button @click="profileMenu===false?profileMenu=true:profileMenu=false" class="profile">{{ username[0] }}</button></div>
      </div>

      <div class="profile_menu" id="profileMenu">
        <div style="color: rgba(152,152,152,0.99)">Учетная запись</div>
        <hr  style="width: 230px; margin: 0 auto">
        <div class="profile_icon">
          <div class="icon" style="margin-left: 10px">{{username[0]}}</div>
          <div style="display: flex; flex-direction: column; margin-left: 10px">
            <div style="display: flex;">{{username}}</div>
            <div style="color: rgba(152,152,152,0.99); font-size: 12px">{{email}}</div>
          </div>
        </div>
        <hr  style="width: 230px; margin: 0 auto">
        <div class="profile_text">Профиль и доступ</div>
        <div class="profile_text">Действия</div>
        <div class="profile_text">Карточки</div>
        <div class="profile_text">Настройки</div>
      </div>
    </div>
  </div>
</template>
<!---->
<script>
import {mapState} from "vuex";

export default {
  data(){
    return{
      profileMenu: false
    }
  },
  watch: {
    profileMenu(){
      this.profileMenu?
          document.getElementById('profileMenu').style.display = "flex":
          document.getElementById('profileMenu').style.display = "none"
    }
  },
  computed: {
    ...mapState({
      username: state => state.user.username,
      email: state => state.user.email,
    }),
  },
}
</script>

<style scoped>
.navbar{
  height: 50px;
  background-color: #2e60b9;
  display: flex;
  align-items: center;
  color: white;
}
.btn {
  color: white;
}

.btn:hover{
  color: #b1c6ee;
}
.myInput{
  border-radius: 8px;
  color: white;
  background-color: #b1c6ee;
  padding-bottom: 5px;
  padding-top: 5px;
  padding-left: 10px;
  border: 0;
  border: none;
  margin-left: 500px;
}
::placeholder{
  color: white;
}
.profile{
  margin-left: 40px;
  border-radius: 50%;
  border: 0;
  width: 30px;
  height: 30px;
  color: white;
  background-color: #2f73ec;
}

.profile_menu{
  display: none;
  gap: 5px;
  flex-direction: column;
  width: 250px;
  color: black;
  height: 450px;
  background-color: white;
  border-radius: 3px;
  position: absolute;
  top: 55px;
  right: 2px;
  box-shadow: -5px 6px 10px rgba(155, 153, 153, 0.99);
}

.profile_text{
  box-sizing: border-box;
  width: 100%;
  height: 2rem;
  font-size: 14px;
  display: flex;
  align-items: center;
  padding-left: 1rem;

}

.profile_text:hover{
  background-color: #ff050c;
}

.profile_icon{
  display: flex;
}

.icon{
  border-radius: 50%;
  align-items: center;
  font-size: 28px;
  width: 50px;
  height: 50px;
  color: white;
  background-color: #0c50c9;
  display: flex;
  justify-content: center;
}


</style>