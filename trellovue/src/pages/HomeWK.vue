<template>
  <navbar></navbar>
  <div style="display: flex">
    <right_-navbar></right_-navbar>
    <div class="main_home" @click="setProfileMenu(false)">
      <WkConst></WkConst>
      <div style="padding: 0px 0px 0px 120px">
        <div style="display: flex; align-items: center">
          <img src="@/static/images/profile.svg" alt="" style="width: 30px; margin-right: 10px"/>
          <span style="font-weight: 700; font-size: 24px">Мои доски</span>
        </div>
        <div style="display: flex; margin-top: 20px">
          <div v-for="board in boards" class="board">
              <span style="font-weight: 700; color: white; font-size: 16px">{{ board.title }}</span>
          </div>
          <div class="board" style="background-color: rgba(119,136,129,0.38); text-align: center">
              <span style="display: inline-block; vertical-align: middle">Создать доску</span>
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
import {mapActions, mapMutations, mapState} from "vuex";
import axios from "axios";
import Cookies from "js-cookie";
import WkConst from "@/components/UI/WkConst";


export default {
  components: {MyButton, Navbar, Right_Navbar, WkConst},
  data() {
    return {
      workspaces: '',
      boards: '',
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
      })
      axios.get(`http://127.0.0.1:8000/api/v1/get_boards/${id}`, {
        headers: {
          'Authorization': `Token ${Cookies.get('token')}`
        }
      }).then(res => {
        this.boards = res.data
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

.board {
  width: 200px;
  height: 120px;
  border-radius: 5px;
  background-color: #ee7474;
  margin-right: 10px;
  padding: 10px;
}
.board:before {
  content: '';
  display: inline-block;
  height: 100%;
  vertical-align: middle;
}
.board:hover{
  background: rgba(69, 79, 75, 0.51);
}
</style>