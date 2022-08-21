<template>
  <div>
    <div class="register_form">
    <form @submit.prevent>
      <h2>Register Form</h2>
      <div class="form-group">
        <div class="form-group">
          <input v-model="form.username"
                 type="text" class="form-control" id="exampleUsername" placeholder="Username">
        </div>
        <div class="form-group">
          <input v-model="form.first_name"
                 type="text" class="form-control" id="examleFirst_name" placeholder="First_name">
        </div>
        <input v-model="form.email"
            type="email"
               class="form-control"
               id="exampleInputEmail1"
               aria-describedby="emailHelp"
               placeholder="Enter email">
      </div>
      <div class="form-group">
        <input v-model="form.password1"
               :type="place" class="form-control" id="exampleInputPassword1" placeholder="Password">
        <button @mousedown="place='text'" @mouseup="place='password'" class="form-control" type="button">г</button>
      </div>
      <div class="errors">
        {{ password1Error }}
      </div>
      <div class="form-group">
        <input v-model="form.password2"
               type="password" class="form-control" id="exampleInputPassword2" placeholder="Repeat Password">
      </div>
      <div class="errors">{{ errors }}</div>
      <button @click='sendPostRegister' type="submit" class="btn btn-primary">Submit</button>

    </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  components: {
  },
  data() {
    return {
      token: '',
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
      sendPostRegister(){
      if ((this.form.password1 === this.form.password2) && this.formValid){
        axios.post('http://127.0.0.1:8000/api/v1/register', {
            username: this.form.username,
            email: this.form.email,
            password1: this.form.password1,
            password2: this.form.password2,
            first_name: this.form.first_name
        }).then(res => {
          console.log(res.data.status)
          if (Number(res.data.status) === 123){
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
  },
  watch: {
    'form.password1'(){
      if (this.form.password1.length < 6){
        this.password1Error = 'Пароль слишком короткий'
      }
      else {
        this.password1Error = ''
      }
      if (this.form.password1.length > 5) {
        if (parseInt(this.form.password1.search(/\d/)) === -1) {
          this.password1Error = 'Пароль должен содержать цифры'
        } else {
          this.password1Error = ''
          this.formValid = true
        }
      }
    }

  }

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
