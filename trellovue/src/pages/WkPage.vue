<template>
  <navbar></navbar>
  <div>
    <h1>Hi</h1>
    <h2>{{ this.$route.params.slug }}</h2>
  </div>
</template>

<script>
import Navbar from "@/components/UI/Navbar";
export default {
  components: {Navbar}
}
</script>

<style scoped>

</style>