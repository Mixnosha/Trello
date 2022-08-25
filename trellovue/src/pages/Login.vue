<template>
  <div>
    <div class="register_form">
      <form @submit.prevent>
        <h2>Login</h2>

        <div class="form-group">
          <div class="form-group">
            <my-input v-focus v-model="form.username"
                      @keyup.enter="nextFocus"
                      type="text" class="form-control" id="1" placeholder="Username"/>
          </div>
          <div class="form-group">
            <my-input
                id="2"
                @keyup.enter="nextFocus"
                v-model="form.password"
                placeholder="Password"
                :type="place"
            />

            <my-button
                @mousedown="place='text'"
                @mouseup="place='password'"
                type="button">г
            </my-button>
          </div>
          <my-button @click="sendLogin" type="submit">Login</my-button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import {mapActions, mapMutations} from "vuex";

export default {
  data() {
    return {
      form: {
        username: '',
        password: '',
      },
      place: "Password",
    }
  },
  methods: {
    ...mapMutations({
      setUsername: 'user/setUsername',
      setPassword: 'user/setPassword',
    }),
    ...mapActions({
      Login: 'user/Login',
    }),
    // nextFocusLog(el) {
    //   if (el.target.id === '2') {
    //     this.sendLogin()
    //   } else {
    //     document.getElementById(Number(el.target.id) + 1).focus()
    //   }
    // },

  }
}
</script>

<style scoped>

</style>