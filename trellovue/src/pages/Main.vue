<template>
  <div style="text-align: left">
    <div v-if="!username">
      <my-button @click="$router.push('/register')">Register</my-button>
      <my-button @click="$router.push('/login')">Login</my-button>
    </div>
    <div v-else>
    </div>
    <div>Рабчие пространства <span @click="addWorkspace">+</span></div>
    <div v-for="wk in workspaces" style="display: flex">
      <img :src="wk.logo" alt="" width="30" height="30"><strong><div :id="wk.id">{{wk.title}}</div></strong>
    </div>
  </div>
</template>
<script>
import MyButton from "@/components/UI/MyButton";
import {mapState} from "vuex";

export default {
  components: {MyButton},
  data() {
    return {
      workspaces: '',
    }
  },
  methods: {
    addWorkspace(){
      console.log('sdfsdf')
    },
  },
  computed: {
    ...mapState({
      username: state => state.user.username,
    }),
  },
}
</script>

<style scoped>

</style>