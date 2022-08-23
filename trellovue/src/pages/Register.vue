<template>
  <div>
    <h1>{{ username }}</h1>
    <h1>{{ pass }}</h1>
    <h1> {{ token }}</h1>
    <div class="register_form">
    <form @submit.prevent>
      <h2>Register Form</h2>

      <div class="form-group">
        <div class="form-group">
          <my-input v-focus v-model="form.username"
                    @keyup.enter="nextFocus"
                 type="text" class="form-control" id="1" placeholder="Username"/>
        </div>

        <div class="form-group">
          <my-input v-model="form.first_name"
                 type="text"
                    @keyup.enter="nextFocus"
                    class="form-control"
                    id="2"
                    placeholder="First_name"/>
        </div>

        <my-input v-model="form.email"
            type="email"
                  id="3"
                  @keyup.enter="nextFocus"
               class="form-control"
               aria-describedby="emailHelp"
               placeholder="Enter email"/>
      </div>

      <div class="form-group">
        <my-input
            id="4"
            @keyup.enter="nextFocus"
            v-model="form.password1"
            placeholder="Password"
            :type="place"
        />

        <my-button
            @mousedown="place='text'"
            @mouseup="place='password'"
            type="button">г
        </my-button>
      </div>

      <div class="errors">
        {{ password1Error }}
      </div>

      <div class="form-group">
        <my-input v-model="form.password2"
                  id="5"
                  @keyup.enter="nextFocus"
               type="password"
               placeholder="Repeat Password"
        />
      </div>

      <div class="errors">{{ errors }}</div>
      <my-button @click="sendPostRegister" type="submit">Register</my-button>
    </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import {mapState, mapGetters, mapActions, mapMutations} from 'vuex'

export default {
  data() {
    return {
      errors: '',
      password1Error: '',
      formValid: false,
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
    }),
    ...mapActions({
      Login: 'user/Login',
    }),
      sendPostRegister(){
      if ((this.form.password1 === this.form.password2) && this.formValid){
        axios.post('http://192.168.100.6:8000/api/v1/register', {
            username: this.form.username,
            email: this.form.email,
            password1: this.form.password1,
            password2: this.form.password2,
            first_name: this.form.first_name
        }).then(res => {
          if (String(res.data.status) === 'true'){
              this.setUsername(this.form.username)
              this.setPassword(this.form.password1)
              this.Login()
              this.$router.push({name: 'main'})

          }
          else if (Number(res.data.status) === 123){
            this.errors = 'Имя пользователя уже занято'
          }
        }).catch(error => {
          console.log(error)
        });
      }
      else {
          this.errors = 'Пароли не совпадают'
          this.form.password2 = ''
          this.form.password1 = ''
      }

    },
    nextFocus(el){
      if (el.target.id === '5'){
        this.sendPostRegister()
      }
      else{
        document.getElementById(Number(el.target.id) + 1).focus()
      }


    }

  },
  watch: {
    'form.password1'(){
      if (this.form.password1.length < 8){
        this.password1Error = 'Пароль слишком короткий'
      }
      else {
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
      pass: state => state.user.password,
      token: state => state.user.token,
    }),
  },
}


</script>

<style scoped>
.register_form{
  margin-left: 35%;
  width: 400px;
  height: 500px;
  align-items: center;
  justify-content: center;
  display: flex;
}
.form-control{
  margin-bottom: 5px;
}
.errors{
  color: #ff050c;
}
</style>
