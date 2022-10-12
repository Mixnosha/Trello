<template>
  <navbar></navbar>
  <div style="display: flex">
  <right_-navbar></right_-navbar>
  <div class="main_home"  @click="setProfileMenu(false)">

  </div>

  </div>
</template>
<script>
import MyButton from "@/components/UI/MyButton";
import {mapMutations, mapState} from "vuex";
import Navbar from "@/components/UI/Navbar"
import Right_Navbar from "@/components/UI/Right_Navbar";

export default {
  components: {MyButton, Navbar, Right_Navbar},
  data() {
    return {
      workspaces: '',
    }
  },
  methods: {
    ...mapMutations({
      setProfileMenu: 'navbar/setProfileMenu',
    }),
  },
  computed: {
    ...mapState({
      username: state => state.user.username,
      profileMenu: state => state.navbar.profileMenu,
    }),
  },

}
</script>

<style scoped>

</style>