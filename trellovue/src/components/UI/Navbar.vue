<template>
  <header>
    <div class="header__logo">Trello</div>
    <nav class="header__nav">
      <div class="nav__btn">Рабочие пространства<img src="@/static/images/arrow.svg" class="nav__btn-svg"></div>
      <div class="nav__btn">Недавние<img src="@/static/images/arrow.svg" class="nav__btn-svg"></div>
      <div class="nav__btn">В избранном<img src="@/static/images/arrow.svg" class="nav__btn-svg"></div>
      <div class="nav__btn_create" style="">Создать</div>
    </nav>
    <div class="header__profile">
      <input type="text" class="profile-input" placeholder="Поиск">
      <div class="profile-icon" @click="profileVisible">{{ username[0] }}</div>
    </div>
  </header>
  <div class="wk__open">
    <div class="wk__label" style="padding: 8px; font-size: 14px">Рабочие пространства</div>
    <hr style="width: 300px; margin: 0 auto">
    <div class="current_wk">
      <div class="current_lbl" style="font-size: 12px; color: rgba(126,125,125,0.99); font-weight: 700">
        Текущее рабочее пространство
      </div>
      <div style="display:flex; align-items: center; padding-left: 8px">
        <img src="@/static/images/wks.svg" width="38px" style="border-radius: 4px">
        <div style="padding-left: 6px">Tako</div>
      </div>
    </div>
    <hr style="width: 100%; margin: 0 auto">
    <div class="your__wk" style="padding-top: 10px; padding-bottom: 16px">
      <div class="current_lbl"
           style="padding-left: 7px;font-size: 12px; color: rgba(126,125,125,0.99); font-weight: 700;">Ваши рабочие
        пространства
      </div>

      <div style="padding-left: 12px; padding-right: 12px">
        <div v-for="wk in workspaces" class="some-wk" style="display:flex; align-items: center; padding-left: 8px">
          <img src="@/static/images/wks.svg" width="38" style="border-radius: 4px">
          <div style="padding-left: 6px">{{ wk.title }}</div>
        </div>
      </div>
    </div>
  </div>
  <div class="profile_menu" id="profileMenu">
    <div style="color: rgba(152,152,152,0.99); padding-left: 25%">Учетная запись</div>
    <hr style="width: 230px; margin: 0 auto">
    <div class="profile_icon">
      <div class="icon" style="margin-left: 10px">{{ username[0] }}</div>
      <div style="display: flex; flex-direction: column; margin-left: 10px">
        <div style="display: flex;">{{ username }}</div>
        <div style="color: rgba(152,152,152,0.99); font-size: 12px">{{ email }}</div>
      </div>
    </div>
    <hr style="width: 230px; margin: 0 auto">
    <div class="profile_text">Профиль и доступ</div>
    <div class="profile_text">Действия</div>
    <div class="profile_text">Карточки</div>
    <div class="profile_text">Настройки</div>
    <hr style="width: 230px; margin: 0 auto">
    <div @click="Logout" class="profile_text">Выйти</div>
  </div>
</template>
<script>
import {mapMutations, mapState} from "vuex";
import axios from "axios";
import Cookies from "js-cookie";

export default {
  data() {
    return {}
  },
  watch: {
    profileMenu() {
      this.profileMenu ?
          document.getElementById('profileMenu').style.display = "flex" :
          document.getElementById('profileMenu').style.display = "none"
    }

    /// написать открытие через реактивные классы
  },
  methods: {
    ...mapMutations({
      setToken: 'user/setToken',
      setEmail: 'user/setEmail',
      setUsername: 'user/setUsername',
      setProfileMenu: 'navbar/setProfileMenu',
      setWk__visible: 'navbar/setWk__visible',
    }),
    profileVisible() {
      if (this.profileMenu === false) {
        this.setProfileMenu(true)
      } else {
        this.setProfileMenu(false)
      }
    },
    async loadEmail() {
      this.setToken(Cookies.get('token'))
      this.setUsername(Cookies.get('username'))
      const res = await axios.get('http:///192.168.100.6:8000/api/v1/auth/users', {
        headers: {
          'Authorization': `Token ${this.token}`
        }
      })
      const email = res.data[0].email
      this.setEmail(email)
      Cookies.set('email', email)
    },
    Logout() {
      axios.post("http://192.168.100.6:8000/api/v1/auth/token/logout", {}, {
        headers: {
          'Authorization': `Token ${this.token}`
        }
      }).then(res => {
        if (res.status === 204) {
          Cookies.remove('username')
          Cookies.remove('token')
          Cookies.remove('email')
          this.$router.push({name: 'register'})
        }
      })
    },
  },
  computed: {
    ...mapState({
      username: state => state.user.username,
      token: state => state.user.token,
      email: state => state.user.email,
      profileMenu: state => state.navbar.profileMenu,
      workspaces: state => state.navbar.workspaces,
      wk__visible: state => state.navbar.wk__visible,
    }),
  },
  mounted() {
    this.loadEmail()
  }
}
</script>

<style scoped>
.header__logo {
  font-weight: 700;
}

.profile_menu {
  display: none;
  gap: 5px;
  flex-direction: column;
  width: 250px;
  color: black;
  height: 300px;
  background-color: white;
  border-radius: 3px;
  position: absolute;
  top: 55px;
  right: 2px;
  box-shadow: -5px 6px 10px rgba(155, 153, 153, 0.99);
}

.profile_text {
  box-sizing: border-box;
  width: 100%;
  height: 2rem;
  font-size: 14px;
  display: flex;
  align-items: center;
  padding-left: 1rem;
  cursor: pointer;

}

.profile_text:hover {
  background-color: rgba(160, 163, 168, 0.09);
}

.profile_icon {
  display: flex;
}

::placeholder {
  color: white;
}

.icon {
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

<style scoped>
header {
  width: 100%;
  height: 44px;
  background: #026AA7;
  color: white;
  display: flex;
  align-items: center;
  padding: 15px;
}

.header__nav {
  display: flex;
  gap: 1rem;
  margin-left: 1rem;
}

.nav__btn_create {
  display: flex;
  justify-content: center;
  align-items: center;
  width: auto;
  height: 100%;
  padding: 5px 10px;
  background: rgba(23, 43, 77, 0.45);
  transition: background-color 32ms;
  border-radius: 4px;
}

.nav__btn {
  display: flex;
  justify-content: center;
  align-items: center;
  width: auto;
  height: 100%;
  padding: 5px 10px;
  transition: background-color 32ms;
  border-radius: 4px;
}

.nav__btn:hover {
  background: rgba(150, 180, 231, 0.32);
}

.nav__btn_create:hover {
  background: rgba(150, 180, 231, 0.32);
}

.nav__btn-svg {
  margin-left: 5px;
  width: 12px;
}

.header__profile {
  margin-left: auto;
  display: flex;
  gap: 1rem;
  align-items: center;
}

.profile-icon {
  width: 2rem;
  height: 2rem;
  border-radius: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #0c50c9;
  cursor: pointer;
}

.profile-input {
  width: 230px;
  height: 34px;
  outline: none;
  background: rgba(255, 255, 255, 0.2) url("@/static/images/search-icon.svg") no-repeat;
  background-size: 19px;
  background-position: 3% 45%;
  padding-left: 2rem;
  box-sizing: border-box;
  border: 1px solid #4475d9;
  border-radius: 6px;
  color: white;
}


.wk__open {
  margin-top: 3px;
  padding: 0px 0px 2px 0px;
  margin-left: 84px;
  position: absolute;
  width: 320px;
  box-shadow: 1px 1px 8px rgba(155, 153, 153, 0.99);
  background: white;
  border-radius: 4px;

}

.wk__label {
  display: flex;
  justify-content: center;
  color: rgba(152, 152, 152, 0.99);
}

.current_wk {
  padding: 18px 0px 12px 4px;
}

.current_lbl {
  padding-bottom: 12px;
  padding-left: 4px;
}

.some-wk {
  margin-bottom: 12px;
  border-radius: 6px;
}

.some-wk:hover {
  background: rgba(150, 180, 231, 0.32);

}
</style>