<template>
  <navbar></navbar>
  <div>
  <WkLeftMenu></WkLeftMenu>
    <WkConst :wk="wk" :id="id"></WkConst>

  </div>
</template>

<script>
import Navbar from "@/components/UI/Navbar";
import WkLeftMenu from "@/components/UI/WkLeftMenu";
import WkConst from "@/components/UI/WkConst";

export default {
  components: {WkLeftMenu, Navbar, WkConst},

  data(){
    return {

    }
  }
}
</script>

<style scoped>

</style>