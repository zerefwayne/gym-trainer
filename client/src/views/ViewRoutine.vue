<template>
  <div class="app-view-routine">
    <template v-if="!hasLoaded">
      Please wait while your routine loads.
    </template>
    <template v-else>
      <div class="container" :key="randomNumber">
        <div class="routing-heading">
          <div class="display-4 heading">
            {{ routine["userId"]["name"].split(" ")[0] }}'s Routine
          </div>
          <div class="routine-active" v-if="!routine.isRoutineCompleted">
            ACTIVE
          </div>
        </div>
        <div class="routine-selector">
          <div class="week-selector">
            <div class="mini-heading">Week</div>
            <button
              v-for="(week, index) in [1, 2, 3, 4, 5, 6]"
              @click="handleActiveWeek(week)"
              :key="index"
              :class="
                activeWeek == week ? 'week-button' : 'week-button active-week'
              "
            >
              {{ week }}
            </button>
          </div>
          <div class="day-selector">
            <div class="mini-heading">Day</div>
            <button
              v-for="(day, index) in [1, 2, 3, 4, 5, 6, 7]"
              @click="handleActiveDay(day)"
              :key="index"
              :class="activeDay == day ? 'day-button' : 'day-button active-day'"
            >
              {{ day }}
            </button>
          </div>
        </div>
        <div class="selected-day">
          <template v-if="this.selectedDay.isRestDay">
            <img src="@/assets/chill.png" height="150px" />
          </template>

          <template v-else>
            <div
              v-for="(day_exercise, index) in this.selectedDay.exercises"
              :key="index"
            >
              <div class="card exercise">
                <div class="card-body">
                  <div class="details">
                    <div class="difficulty">
                      {{ day_exercise["exercise"]["difficulty"] }}
                    </div>
                    <div class="name">
                      {{ day_exercise["exercise"]["exercise"] }}
                    </div>
                    <div class="body-part">
                      {{ day_exercise["exercise"]["bodyPart"] }}
                    </div>
                    <div class="sets">
                      Sets: {{ day_exercise["exercise"]["sets"] }}
                    </div>
                    <div class="reps">
                      Reps: {{ day_exercise["exercise"]["reps"] }}
                    </div>
                  </div>
                  <div class="actions">
                    <template
                      v-if="
                        !day_exercise['hasGivenFeedback'] &&
                          day_exercise['isExerciseCompleted']
                      "
                    >
                      <button
                        class="like"
                        @click="handleExerciseFeedback(day_exercise, index, 1)"
                      >
                      {{ day_exercise["exercise"]["likes"] }}
                        <img
                          v-if="day_exercise['isExerciseCompleted']"
                          src="@/assets/like.png"
                          height="20px"
                        />
                      </button>
                      <button
                        class="dislike"
                        @click="handleExerciseFeedback(day_exercise, index, 0)"
                      >

                        <img
                          v-if="day_exercise['isExerciseCompleted']"
                          src="@/assets/dislike.png"
                          height="20px"
                        />
                        {{ day_exercise["exercise"]["numberOfVotes"] - day_exercise["exercise"]["likes"] }}
                      </button>
                    </template>
                    <button
                      class="mark-done"
                      @click="handleSetExerciseDone(day_exercise['_id'], index)"
                      :disabled="day_exercise['isExerciseCompleted']"
                    >
                      <img
                        v-if="!day_exercise['isExerciseCompleted']"
                        src="@/assets/unchecked.png"
                        height="20px"
                      />
                      <img
                        v-if="day_exercise['isExerciseCompleted']"
                        src="@/assets/checked.png"
                        height="20px"
                      />
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </template>
        </div>
      </div>
    </template>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "ViewRoutine",
  data() {
    return {
      routine: null,
      hasLoaded: false,
      activeWeek: 1,
      activeDay: 1,
      selectedDay: null,
      randomNumber: 87
    };
  },
  methods: {
    handleActiveWeek(week) {
      this.activeWeek = week;
      this.activeDay = 1;

      this.selectedDay = this.routine["workouts"][this.activeWeek - 1]["days"][
        this.activeDay - 1
      ];
    },

    handleActiveDay(day) {
      this.activeDay = day;

      this.selectedDay = this.routine["workouts"][this.activeWeek - 1]["days"][
        this.activeDay - 1
      ];
    },

    handleExerciseFeedback(day_exercise, index, like) {
      const routineId = this.$route.params.routineId;

      const opts = {
        routine_id: routineId,
        exercise_id: day_exercise["exercise"]["_id"],
        week: this.activeWeek - 1,
        day: this.activeDay - 1,
        index,
        like
      };

      console.log(opts);

      this.$http
        .post("/feedback/", opts)
        .then(({ data }) => {
          const newDocument = data["updatedRoutine"];
          console.log("New document", newDocument);

          this.selectedDay =
            newDocument["workouts"][this.activeWeek - 1]["days"][
              this.activeDay - 1
            ];
        })
        .catch(error => {
          console.log(error);
        });

      console.log("Like", day_exercise["exercise"]["_id"]);
    },

    handleSetExerciseDone(exercise_id, index) {
      console.log(exercise_id);

      const routineId = this.$route.params.routineId;

      this.$http
        .post("/routine/exercise/update", {
          routine: routineId,
          exercise: index,
          week: this.activeWeek - 1,
          day: this.activeDay - 1
        })
        .then(({ data }) => {
          const newDocument = data["updatedDocument"];
          console.log("New document", newDocument);

          this.selectedDay =
            newDocument["workouts"][this.activeWeek - 1]["days"][
              this.activeDay - 1
            ];
        })
        .catch(error => {
          this.hasLoaded = true;
          console.log(error);
        });
    }
  },
  props: {},
  mounted() {
    const routineId = this.$route.params.routineId;

    this.$http
      .post("/routine", { routineId })
      .then(({ data }) => {
        if (data.success) {
          this.routine = data.message;
          // console.table(this.routine);
          // console.log(this.routine);
          this.selectedDay = this.routine["workouts"][0]["days"][0];

          console.log(this.activeDay);
      console.log(this.routine);

          // console.log(this.selectedDay);
        } else {
          console.log(data.message);
        }
        this.hasLoaded = true;
      })
      .catch(error => {
        console.log(error);
      });


  }
});
</script>

<style lang="scss">
.app-view-routine {
  min-height: 100vh;
  max-width: 100%;

  display: flex;
  padding: 4rem;

  .heading {
    margin-top: 6rem;
  }

  .routine-heading {
    display: flex;
  }

  .routine-active {
    padding: 0.5rem 1rem;
    color: green;
    border: 1px solid green;
    width: fit-content;
    border-radius: 2px;
    margin-top: 1rem;
  }

  .routine-selector {
    margin-top: 3rem;

    .mini-heading {
      font-size: 2rem;
      color: #555;
    }

    .week-selector {
      display: flex;
      flex-direction: row;

      .week-button {
        margin-left: 1.5rem;
        background-color: white;
        border: none;
        border: 1px solid black;
        border-radius: 50%;
        outline: none;
        cursor: pointer;
        height: 3rem;
        width: 3rem;

        &:active {
          border: none;
          outline: none;
        }
      }

      .active-week {
        background-color: black;
        color: white;

        transition: all 200ms ease-in-out;
      }
    }

    .day-selector {
      margin-top: 1.5rem;
      display: flex;
      flex-direction: row;

      .day-button {
        margin-left: 1.5rem;
        background-color: white;
        border: none;
        border: 1px solid #4b7bec;
        border-radius: 50%;
        color: #4b7bec;
        cursor: pointer;
        outline: none;

        height: 3rem;
        width: 3rem;

        &:first-of-type {
          margin-left: 3rem;
        }
      }

      .active-day {
        background-color: #4b7bec;
        color: white;
        transition: all 200ms ease-in-out;
      }
    }
  }

  .selected-day {
    margin-top: 4rem;
  }

  .exercise {
    max-width: 70%;
    margin-bottom: 1rem;
    border-radius: 5px;

    .card-body {
      display: flex;
      justify-content: space-between;
    }
    .details {
      display: flex;
      align-items: center;

      .difficulty {
        text-transform: uppercase;
        font-weight: bold;
        color: #777;
      }

      .name {
        margin-left: 2rem;
        font-size: 1.2rem;
      }

      .body-part {
        margin-left: 1rem;
        text-transform: uppercase;
        font-size: 0.8rem;
        color: white;
        background-color: #4b7bec;
        padding: 3px 0.7rem;
        border-radius: 3px;
      }

      .sets {
        margin-left: 2rem;
        font-size: 1.2rem;
      }

      .reps {
        margin-left: 2rem;
        font-size: 1.2rem;
      }
    }

    .actions {

      display: flex;
      flex-direction: row;

    }

    .mark-done,
    .like,
    .dislike {
      background: none;
      border: none;
      outline: none;
      cursor: pointer;
    }

    .like {
      margin-right: 1rem;
      color: green;
      font-weight: bold;
      display: flex;
      align-items: center;

      img {
        margin-left: 5px;
      }

    }

    .dislike {
      margin-right: 1rem;
      color: red;
      font-weight: bold;
      display: flex;
      align-items: center;

      img {
        margin-right: 5px;
      }
    }
  }
}
</style>
