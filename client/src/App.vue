<template>
  <div id="app">
    <template v-if="hasLoaded">
      <Navbar v-if="!$route.meta.hideNavigation"/>
      <vue-page-transition name="overlay-left-full">
        <router-view></router-view>
      </vue-page-transition>
    </template>
    <template v-else>
      <div class="app-loading">
        Please wait while we load your app.
      </div>
    </template>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Navbar from "./components/Navbar.vue";

export default Vue.extend({
  name: "app",
  components: {
    Navbar
  },
  data() {
    return {
      hasLoaded: false
    };
  },
  mounted() {
    this.$http
      .get("/auth/user")
      .then(response => {
        console.log("Successfully logged in!");
        this.$store.dispatch("initApp", response.data).then(() => {
          this.hasLoaded = true;
          console.log(this.$store.getters.isAuthenticated);
        });
      })
      .catch(error => {
        console.error(error);
      });
  }
});
</script>

<style lang="scss">
#app {
  font-family: "IBM Plex Sans", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.app-loading {
  height: 100vh;
  width: 100%;
  background-color: #060606;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.overlay-left,
.overlay-right,
.overlay-top,
.overlay-bottom {
  background: #060606 !important;
}
</style>
