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
               type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
      </div>
      <div class="form-group">
        <input v-model="form.password2"
               type="password" class="form-control" id="exampleInputPassword2" placeholder="Repeat Password">
      </div>
      <button @click='sendPostRegister' type="submit" class="btn btn-primary">Submit</button>
    </form>
    </div>
    <button type="button" @click='methodAxios'>get</button>
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
      if (true){
        axios.post('http://127.0.0.1:8000/api/v1/register', {
            username: 'Zefa',
            email: 'xmix@fmai.com',
            password1: 'Maksim21z',
            password2: 'Maksim21z',
            first_name: 'Kristina'
        }).then(res => {
          console.log(res.data)
        }).catch(error => {
          console.log(error)
        });
      }
    },
    async workspace(){
      const res = await fetch('http://127.0.0.1:8000/api/v1/workspace/', {
        method: 'GET',
        mode: 'no-cors',
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'Token 275dabc5297e597df589c901b1fdea32779b7d80'
        },
        credentials: 'include',
      })
      console.log(JSON.parse(res))
    },
    methodAxios(){
      axios
          .get('http://127.0.0.1:8000/api/v1/workspace', {
            headers: {
              'Authorization': 'Token 275dabc5297e597df589c901b1fdea32779b7d80',
            }
          })
          .then(response => {console.log(response.data)})
          .catch(error => {console.log(error)});
    },
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
</style>
