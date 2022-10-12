<template>
    <navbar main_color="rgba(28, 28, 28, 0.26)"></navbar>
    <left-bar></left-bar>
    <Body></Body>
</template>

<script>
import Navbar from "@/components/UI/Navbar";
import LeftBar from "@/components/Boards/LeftBar";
import axios from "axios";
import Body from "@/components/Boards/Body";
export default {
  components: {Body, LeftBar, Navbar},
  data(){
    return{
      wk_id: null,
    }
  },
  methods: {

  },

}
</script>

<style scoped>

</style>