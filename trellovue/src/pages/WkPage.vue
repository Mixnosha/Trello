<template>
  <navbar></navbar>
  <main>
   <WkLeftMenu></WkLeftMenu>
    <div class="wk__main">
    <WkConst></WkConst>
      <hr style="width: 96%; margin: 0 auto">
      <div class="boards__wk">
      </div>
    </div>
  </main>
</template>

<script>
import Navbar from "@/components/UI/Navbar";
import WkLeftMenu from "@/components/UI/WkLeftMenu";
import WkConst from "@/components/UI/WkConst";
export default {
  components: {WkLeftMenu, Navbar, WkConst},
  data() {
    return {
    }
  },
  methods: {

  },
  watch: {
  },
  mounted() {
  }
}
</script>

<style scoped>
.wk__main {
  position: relative;
  width: 1200px;
  height: 300px;
  left: 300px;
  top: 60px;
}
</style>