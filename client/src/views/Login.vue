<template>
  <div class="app-login">
    <div class="container">
      <div class="login-container">
        <img src="../assets/logo_login.png" height="150px" />
        <div style="margin-top: 4rem;">
          <button @click="loginHandler" style="outline: none; border: none; background: transparent; cursor: pointer;"><img src="../assets/google.png" height="40px"></button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import axios from "axios";

export default Vue.extend({
  name: "Login",
  props: {},
  methods: {
    loginHandler() {
      window.location.href = "http://localhost:3000/auth/google";
    }
  }
});
</script>

<style lang="scss">
.app-login {
  height: 100vh;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;

  background: url("../assets/login2.jpg");
  background-size: cover;

  .login-container {

    display: flex;
    flex-direction: column;
    align-items: flex-end;
    justify-content: center;

  }

}
</style>
