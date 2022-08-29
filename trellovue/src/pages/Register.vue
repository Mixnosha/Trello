<template>
  <div>
    <div class="register">
      <img src="@/static/images/trello-logo.svg" style="width: 183px; height: 40px  ">
      <div class="register__container">
        <div class="register__title">
          <div v-if="form_status==='log'">Войдите чтобы перейти далее:</div>
          <div v-else style="font-weight: 700">Регистрация аккаунта</div>
          <div v-if="form_status==='log'" style="font-weight: 700">Trello</div>
        </div>
        <div class="register__body">
          <div class="register__input">
            <input v-focus v-model="form.username"
                   @keyup.enter="nextFocusReg"
                   type="text" id="1" class="register__input-field" placeholder="Имя пользователя"/>

            <input v-if="form_status==='reg'" v-model="form.first_name"
                   @keyup.enter="nextFocusReg"
                   type="text" id="2" class="register__input-field" placeholder="Введите ваше имя "/>
            <input v-if="form_status==='reg'" v-model="form.email"
                   @keyup.enter="nextFocusReg"
                   type="email" id="3" class="register__input-field" placeholder="Введите адрес электронной почты"/>
            <input  v-model="form.password1"
                   @keyup.enter="nextFocusReg"
                   :type="place" id="4" class="register__input-field" placeholder="Введите пароль"/>
            <div style="color: #ee7474; font-size: 12px;">
              {{ password1Error }}
            </div>
            <img @click="place==='text'?place='password':place='text'" :src="path_eye" width="40px"
                 class="register__input-field">
            <input v-if="form_status==='reg'" v-model="form.password2"
                   @keyup.enter="nextFocusReg"
                   type="password" id="5" class="register__input-field" placeholder="Повторите пароль"/>
            <div style="color: #ff050c; font-size: 12px">{{ errors }}</div>
            <button @click="sendForm" class="register__input-btn">Продолжить</button>
            <span class="register__input-footer">или</span>
          </div>
          <div class="register_links">
            <div class="register__link">Войти с помщью GitHub</div>
            <hr class="register__links-hr">
          </div>
          <a @click="form_status==='reg'?form_status='log':form_status='reg'" class="regsiter__help">
            <span v-if="form_status==='reg'">У вас уже есть акаунт Trello? Войти</span>
            <span v-else >Регестрация аккаунта</span>
          </a>
        </div>
      </div>
    </div>


  </div>
</template>

<script>
import axios from 'axios';
import {mapState, mapActions, mapMutations} from 'vuex'
import Cookies from "js-cookie";
import eye_cls from '@/static/images/eye-close.svg'
import eye_opn from '@/static/images/eye-open.svg'

export default {
  data() {
    return {
      form_status: 'reg',
      path_eye: eye_cls,
      errors: '',
      tokenForm: '',
      password1Error: '',
      place: 'password',
      form: {
        username: '',
        email: '',
        password1: '',
        password2: '',
        first_name: ''
      },
    }
  },
  methods: {
    ...mapMutations({
      setUsername: 'user/setUsername',
      setPassword: 'user/setPassword',
      setEmail: 'user/setEmail',
    }),
    ...mapActions({
      Login: 'user/Login',
    }),
    async Login(){
      const log_data = await axios.post('http://127.0.0.1:8000/api/v1/auth/token/login/', {
        username: this.form.username,
        password: this.form.password1,
      }).catch(
          this.errors = 'Проверьте имя пользователя или пароль'
      )
      if (log_data.data.auth_token){
        this.$router.push({name: 'main'})
      }
      return log_data.data.auth_token
    },
    async sendForm(){
      if (this.form_status==='reg'){
        const reg_data = await axios.post("http://127.0.0.1:8000/api/v1/register", {
          username: this.form.username,
          first_name: this.form.first_name,
          email: this.form.email,
          password1: this.form.password1,
          password2: this.form.password2,
        })
        console.log(reg_data.status)
        if (reg_data.data.status === 'true'){
          Cookies.set('username', this.form.username, {expires: 90})
          Cookies.set('email', this.form.email, {expires: 90})
          this.Login()
              .then(function (token){
            Cookies.set('token', token, {expires: 90})
          })
          this.$router.push({name: 'main'})
        }
        else if (reg_data.data.status === '123'){
          this.errors = "Имя пользователя уже существует"
          document.getElementById('1').focus()
        }
      }
      else if (this.form_status==='log'){
          this.Login().then(token => {
            Cookies.set('token', token, {expires: 90})
            Cookies.set('username', this.form.username, {expires: 90})
          }
        )
      }
    },
    nextFocusReg(el) {
      if (el.target.id === '5') {
        this.sendForm()
      } else {
        document.getElementById(Number(el.target.id) + 1).focus()
      }
    },
  },
  watch: {
    place() {
      this.place === 'text' ? this.path_eye = eye_opn : this.path_eye = eye_cls
    },
    'form.password1'() {
      if (this.form.password1.length < 8) {
        this.password1Error = 'Пароль слишком короткий'
      } else {
        this.password1Error = ''
      }
      if (this.form.password1.length > 7) {
        if (parseInt(this.form.password1.search(/\d/)) === -1) {
          this.password1Error = 'Пароль должен содержать цифры'
        } else {
          this.password1Error = ''
          this.formValid = true
        }
      }
    },
  },
  computed: {
    ...mapState({
      username: state => state.user.username,
      token: state => state.user.token,
    }),
  },
}


</script>

<style scoped>
.register {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 2rem;
}

.register__container {
  display: flex;
  gap: 1rem;
  flex-direction: column;
  background: white;
  width: 400px;
  box-shadow: rgb(0 0 0 / 10%) 0px 0px 10px;
  padding: 32px 40px;
}

.register__title {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  color: rgb(94, 108, 132);
}

.register__body {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;

}

.register__input {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  width: 100%;
}

.register__input-field {
  outline: none;
  border: 2px solid #dad7d7;
  width: 100%;
  height: 36px;
  border-radius: 5px;
  transition: 0.3s;
}

.register__input-field:hover {
  background: #f1efef;
}

.register__input-field:focus {
  border: 2px solid #0052cc;
}

.register__input-btn {
  width: 100%;
  background: #0052cc;
  color: white;
  border: none;
  height: 36px;
  transition: 0.2s;
}

.register__input-btn:hover {
  background: #0265f8
}

.register__input-footer {
  color: rgb(151, 160, 175);
  font-size: 14px;
  display: flex;
  justify-content: center;
}

.register_links {
  width: 100%;
  font-weight: 700;
  color: #42526e;
}

.register__link {
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: rgb(0 0 0 / 10%) 0px 0px 10px;
  height: 36px;
  width: 100%;
  margin-bottom: 2rem;
  background: url("@/static/images/github-icon.svg") no-repeat;
  background-position: 5% 50%;
  cursor: pointer;
}

.register__links-hr {
  width: 100%;
}

.regsiter__help {
  text-decoration: none;
  cursor: pointer;
}


</style>
