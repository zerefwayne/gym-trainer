<template>
  <div class="app-profile">
    <div class="container">
      <div class="details">
        <img :src="user.displayPhotoUrl" class="photo" />
        <div class="text">
          <div class="name">{{ user.name }}</div>
          <div class="email text-muted">{{ user.email }}</div>
        </div>
      </div>
      <div v-if="currentRoutine" class="current-routine">
        <h4 class="heading display-4">
          Current Routine
        </h4>
        <ul class="list-group">
          <li class="list-group-item" style="display: flex; justify-content: space-between;">
            <div>{{ currentRoutine.dateCreated }}</div>
            <button @click="handleViewRoutine(currentRoutine['_id'])">
              View Routine
            </button>
          </li>
        </ul>
      </div>
      <div class="current-routine">
        <h4 class="heading display-4">
          Previous Routines
        </h4>
        <ul class="list-group">
          <li class="list-group-item" style="display: flex; justify-content: space-between;" v-for="(routine, index) in previousRoutines" :key="index">
            <div v-if="previousRoutines">{{ routine["dateCreated"] }}</div>
            <button @click="handleViewRoutine(routine['_id'])">
              View Routine
            </button>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { mapState, mapGetters } from "vuex";

export default Vue.extend({
  name: "Profile",
  data() {
    return {
      currentRoutine: null,
      previousRoutines: null
    };
  },
  methods: {
    handleViewRoutine(routineId) {
      this.$router.push({ name: "view-routine", params: { routineId } });
    }
  },
  async mounted() {
    await this.$http
      .get("/routine/current")
      .then(({ data }) => {
        this.currentRoutine = data.message;
      })
      .catch(error => {
        console.log(error);
      });

    await this.$http
      .get("/routine/completed")
      .then(({ data }) => {
        this.previousRoutines = data.message;
      })
      .catch(error => {
        console.log(error);
      });
  },
  computed: mapState(["user"])
});
</script>

<style lang="scss">
.app-profile {
  min-height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-top: 10rem;

  .details {
    display: flex;
    flex-direction: row;
    align-items: center;

    .text {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      margin-left: 3rem;
    }

    .photo {
      height: 100px;
      border-radius: 50%;
    }

    .email {
      font-size: 1.6rem;
    }

    .name {
      font-size: 3rem;
    }
  }

  .current-routine {
    margin-top: 2rem;

    .heading {
      font-size: 2rem;
    }
  }
}
</style>
