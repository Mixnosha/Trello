<template>
  <div>
    <h1>Main Page</h1>
    <div v-if="!username">
      <my-button @click="$router.push('/register')">Register</my-button>
      <my-button @click="$router.push('/login')">Login</my-button>
    </div>
    <div v-else>
      <my-button @click="Logout">Logout</my-button>
      {{ username }}
    </div>

    <div>Рабчие пространства <span @click="addWorkspace">+</span></div>
    <div v-for="wk in workspaces">
      <img :src="wk.logo" alt="" width="30" height="30"><strong><div :id="wk.id">{{wk.title}}</div></strong>
    </div>
  </div>
</template>

<script>
import {mapActions, mapMutations, mapState} from "vuex";
import MyButton from "@/components/UI/MyButton";
import axios from "axios";
import Cookies from "js-cookie";

export default {
  components: {MyButton},
  data() {
    return {
      workspaces: ''
    }
  },
  methods: {
    ...mapMutations({
      setUsername: 'user/setUsername',
      setToken: 'user/setToken',
    }),
    addWorkspace(){
      console.log('sdfsdf')
    },
    loadData() {
      this.setUsername(Cookies.get('username'))
      this.setToken(Cookies.get('token'))
      axios.get('http://192.168.100.6:8000/api/v1/workspace/', {
        headers: {
          'Authorization': `Token ${this.token}`
      }
      })
          .then(res => {
            console.log(res.data)
            this.workspaces = res.data
          })

    },
    Logout() {
      axios.post("http://192.168.100.6:8000/api/v1/auth/token/logout", {}, {
        headers: {
          'Authorization': `Token ${this.token}`
        }
      }).then(res => {
        if (res.status === 204){
          console.log('dfsfsfsd')
          Cookies.remove('username')
          Cookies.remove('token')
          location.reload();
        }
      })
    }
  },
  computed: {
    ...
        mapState({
          username: state => state.user.username,
          token: state => state.user.token,
        }),
  }
  ,
  mounted() {
    this.loadData()
  }


}
</script>

<style scoped>

</style>