<template>
  <navbar></navbar>
  <div style="display: flex">
    <right_-navbar></right_-navbar>
    <div class="main_home"  @click="setProfileMenu(false)">
      <div class="wk_title">
        <div class="wk_title-image">
          <img src="" alt="">
          <h1>{{ workspaces.title }}</h1>
        </div>
        <div class="wk_title-text">
          <div class="main_title">
            <span></span>
            <img src="" alt="">
          </div>
          <div class="descrip">
            <img src="" alt="">
            <span></span>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import MyButton from "@/components/UI/MyButton";
import Navbar from "@/components/UI/Navbar";
import Right_Navbar from "@/components/UI/Right_Navbar";
import {mapMutations, mapState} from "vuex";
import axios from "axios";
import Cookies from "js-cookie";

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
    get_data(id){
      axios.get(`http://127.0.0.1:8000/api/v1/workspace/${id}`, {
        headers:{
          'Authorization': `Token ${Cookies.get('token')}`
        }
      }).then(res => {
        this.workspaces = res.data
      })

    }
  },
  computed: {
    ...mapState({
      username: state => state.user.username,
      profileMenu: state => state.navbar.profileMenu,
    }),
  },
  mounted() {
    this.get_data(Number(this.$route.params.slug.substring(this.$route.params.slug.length - 2)))
  }


}
</script>

<style scoped>
.main_home{
  width: 100%;
  height: 800px;
  position: absolute;
  margin-top: 45px;
  margin-left: 350px;
  padding: 60px 0px 0px 40px;
}
</style>