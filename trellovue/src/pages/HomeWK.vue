<template>
  <navbar></navbar>
  <div style="display: flex">
    <right_-navbar></right_-navbar>
    <div class="main_home" @click="setProfileMenu(false)">
      <WkConst></WkConst>
      <div style="padding: 0px 0px 0px 120px">
        <div style="display: flex; align-items: center">
          <img
            src="@/static/images/profile.svg"
            alt=""
            style="width: 30px; margin-right: 10px"
          />
          <span style="font-weight: 700; font-size: 24px">Мои доски</span>
        </div>
        <div>
          <div v-for="board in boards">
            <div style="display: flex; margin-top: 20px">
              <div v-for="b in board" class="board">
                <span style="font-weight: 700; color: white; font-size: 16px">{{
                  b.title
                }}</span>
              </div>
            </div>
          </div>
          <div
            class="create_board"
            style="text-align: center"
            @click="
              create_board_form === 'none'
                ? (create_board_form = 'block')
                : (create_board_form = 'none')
            "
          >
            <span style="display: inline-block; vertical-align: middle"
              >Создать доску</span
            >
          </div>
        </div>
      </div>
      <div
        class="main_form_add_board"
        :style="{ display: create_board_form }"
        id="main_form_add_board"
      >
        <CreateBoard :id="this.id"></CreateBoard>
      </div>
    </div>
  </div>
</template>

<script>
import MyButton from "@/components/UI/MyButton";
import Navbar from "@/components/UI/Navbar";
import Right_Navbar from "@/components/UI/Right_Navbar";
import { mapActions, mapMutations, mapState } from "vuex";
import axios from "axios";
import Cookies from "js-cookie";
import WkConst from "@/components/UI/WkConst";
import CreateBoard from "@/components/HomeWK/CreateBoard";

export default {
  components: { CreateBoard, MyButton, Navbar, Right_Navbar, WkConst },
  data() {
    return {
      id: 1,
      workspaces: "",
      boards: "",
      create_board_form: "none",
      width: 0,
    };
  },
  methods: {
    ...mapMutations({
      setProfileMenu: "navbar/setProfileMenu",
      setId: "oneWk/setWkId",
    }),
    ...mapActions({
      loadWk: "oneWk/loadWk",
    }),
    get_data(id) {
      this.setId(id);
      this.loadWk();
      console.log(id);
      axios
        .get(`http://127.0.0.1:8000/api/v1/workspace/${id}`, {
          headers: {
            Authorization: `Token ${Cookies.get("token")}`,
          },
        })
        .then((res) => {
          this.workspaces = res.data;
        });
      axios
        .get(`http://127.0.0.1:8000/api/v1/get_boards/${id}`, {
          headers: {
            Authorization: `Token ${Cookies.get("token")}`,
          },
        })
        .then((res) => {
          let counter = 0;
          let stat = 0;
          let data = [];
          for (const x of Array(Math.ceil(res.data.length / 3) + 1).keys()) {
            data.push([]);
          }
          for (const i of res.data) {
            if (counter === 3) {
              stat += 1;
              counter = 0;
              data[stat].push(i);
            } else {
              data[stat].push(i);
            }
            counter += 1;
          }
          this.boards = data;
        });
    },
  },
  computed: {
    ...mapState({
      username: (state) => state.user.username,
      profileMenu: (state) => state.navbar.profileMenu,
      id: (state) => state.oneWk.id,
    }),
  },
  mounted() {
    document.getElementById("main_form_add_board").style.height = `${
      window.innerHeight - 60
    }px`;
    this.id = Number(
      this.$route.params.slug.substring(this.$route.params.slug.length - 1)
    );
    console.log(this.id);
    this.get_data(this.id);
  },
};
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
.create_board {
  width: 200px;
  height: 120px;
  border-radius: 5px;
  background-color: rgba(119, 136, 129, 0.38);
  margin-right: 10px;
  padding: 10px;
}
.create_board:before {
  content: "";
  display: inline-block;
  height: 100%;
  vertical-align: middle;
}
.create_board:hover {
  background-color: rgba(119, 136, 129, 0.66);
}

.main_form_add_board {
  width: 395px;
  background: white;
  position: absolute;
  border-radius: 4px;
  left: 50%;
  top: 1%;
  box-shadow: -5px 6px 10px rgba(155, 153, 153, 0.99);
  padding: 14px;
  overflow: scroll;
}
</style>
