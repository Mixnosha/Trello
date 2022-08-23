<template>
  <div>
    <h1>Main Page</h1>
    <div v-if="!username">
      <my-button @click="$router.push('/register')">Register</my-button>
      <my-button @click="$router.push('/register')">Login</my-button>
    </div>
    <div v-else>
      <my-button @click="Logout">Logout</my-button>
      {{ username }}
    </div>
  </div>
</template>

<script>
import {mapActions, mapMutations, mapState} from "vuex";
import MyButton from "@/components/UI/MyButton";

export default {
  components: {MyButton},
  data() {
    return {}
  },
  methods: {
    ...mapMutations({
      setUsername: 'user/setUsername',
      setToken: 'user/setToken',
    }),
    get_cookie(cookie_name) {
      let results = document.cookie.match('(^|;) ?' + cookie_name + '=([^;]*)(;|$)');

      if (results)
        return results[2];
      else
        return null;
    },
    loadData() {
      this.setUsername(this.get_cookie("username"))
      this.setToken(this.get_cookie("token"))
    }
  },
  computed: {
    ...mapState({
      username: state => state.user.username,
      token: state => state.user.token,
    }),
  },
  mounted() {
    this.loadData()
  }


}
</script>

<style scoped>

</style>