<template>
  <div>
    <router-view></router-view>
  </div>
</template>

<script>
import Navbar from "@/components/UI/Navbar";
import {mapMutations, mapState} from "vuex";
import Cookies from "js-cookie";
import axios from "axios";

export default {
  components: {Navbar},
  methods: {
    ...mapMutations({
      setUsername: 'user/setUsername',
      setToken: 'user/setToken',
      setEmail: 'user/setEmail'
    }),
    loadData() {
      this.setToken(Cookies.get('token'))
      this.setUsername(Cookies.get('username'))

    },
  },
  computed: {
    ...mapState({
      token: state => state.user.token,
    })
  },
  mounted() {
    this.loadData()
  }
}
</script>
<style>
body{
  overflow-x:hidden;
  overflow-y: hidden;

}
</style>