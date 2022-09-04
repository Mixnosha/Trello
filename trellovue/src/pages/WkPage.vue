<template>
  <navbar></navbar>
  <main>
   <WkLeftMenu></WkLeftMenu>
    <div class="wk__main">
    <WkConst :wk="wk" :id="id"></WkConst>
      <hr style="width: 96%; margin: 0 auto">
      <div class="boards__wk">
      </div>
    </div>
  </main>
</template>

<script>
import Navbar from "@/components/UI/Navbar";
import axios from "axios";
import Cookies from "js-cookie";
import WkLeftMenu from "@/components/UI/WkLeftMenu";
import WkConst from "@/components/UI/WkConst";
export default {
  components: {WkLeftMenu, Navbar, WkConst},
  data() {
    return {
      wk: {
        title: '',
        logo: '',
        status: '',
        description: '',
        slug: '',
        web_site: '',
      },
      id: '',
    }
  },
  methods: {
    async loadWk() {
      this.id = Number(this.$route.params.slug.substring(this.$route.params.slug.length - 2))
      const res = await axios.get(`http://127.0.0.1:8000/api/v1/workspace/${this.id}`, {
        headers: {
          'Authorization': `Token ${Cookies.get('token')}`
        }
      })
      this.wk.title = res.data.title
      this.wk.logo = res.data.logo
      this.wk.status = res.data.status.title
      this.wk.description = res.data.description
      this.wk.slug = res.data.slug
      this.wk.web_site = res.data.web_site
    },

  },
  watch: {
  },
  mounted() {
    this.loadWk()
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