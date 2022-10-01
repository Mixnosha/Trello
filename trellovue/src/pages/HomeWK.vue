<template>
  <navbar></navbar>
  <div style="display: flex">
    <right_-navbar></right_-navbar>
    <div class="main_home" @click="setProfileMenu(false)">
      <WkConst></WkConst>
      <hr>
    </div>
    </div>
</template>

<script>
import MyButton from "@/components/UI/MyButton";
import Navbar from "@/components/UI/Navbar";
import Right_Navbar from "@/components/UI/Right_Navbar";
import {mapActions, mapMutations, mapState} from "vuex";
import axios from "axios";
import Cookies from "js-cookie";
import WkConst from "@/components/UI/WkConst";


export default {
  components: {MyButton, Navbar, Right_Navbar, WkConst},
  data() {
    return {
      workspaces: '',
    }
  },
  methods: {
    ...mapMutations({
      setProfileMenu: 'navbar/setProfileMenu',
      setId: 'oneWk/setWkId',
    }),
    ...mapActions({
      loadWk: 'oneWk/loadWk'
    }),

    get_data(id) {
      this.setId(id)
      this.loadWk()
      axios.get(`http://127.0.0.1:8000/api/v1/workspace/${id}`, {
        headers: {
          'Authorization': `Token ${Cookies.get('token')}`
        }
      }).then(res => {
        this.workspaces = res.data
        console.log(res.data)
      })

    }
  },
  computed: {
    ...mapState({
      username: state => state.user.username,
      profileMenu: state => state.navbar.profileMenu,
      id: state => state.oneWk.id
    }),
  },
  mounted() {

    this.get_data(Number(this.$route.params.slug.substring(this.$route.params.slug.length - 2)))
  }


}
</script>

<style scoped>
.main_home {
  width: 100%;
  height: 800px;
  position: absolute;
  margin-top: 45px;
  margin-left: 350px;
  padding: 40px 0px 0px 0px;
}
</style>