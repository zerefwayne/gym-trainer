<template>
    <div class="view-plan">
        <div class="container">
            <h3 class="display-4 heading">Your new plan is ready!</h3>

            <div class="calculated-data">
                <div class="card data-item">
                    <div class="card-body">
                        <h5 class="card-title">
                            BMI
                        </h5>
                        <h6 class="card-subtitle mb-2 text-muted">Your calculated BMI</h6>
                        <div class="card-text">
                            <h4 class="display-4 mt-2">{{ calculated_data.bmi }}</h4>
                        </div>
                    </div>
                </div>
                <div class="card data-item">
                    <div class="card-body">
                        <h5 class="card-title">
                            Current Fitness
                        </h5>
                        <h6 class="card-subtitle mb-2 text-muted">Based on your data</h6>
                        <div class="card-text">
                            <h4 class="display-4 mt-2">{{ calculated_data.current_fitness }}</h4>
                        </div>
                    </div>
                </div>
                <div class="card data-item">
                    <div class="card-body">
                        <h5 class="card-title">
                            Goal Fitness
                        </h5>
                        <h6 class="card-subtitle mb-2 text-muted">Based on your goals</h6>
                        <div class="card-text">
                            <h4 class="display-4 mt-2">{{ calculated_data.goal_fitness }}</h4>
                        </div>
                    </div>
                </div>
            </div>

            <div style="margin: 2rem 0;">
                <button class="btn btn-success" @click="handleConfirmPlan">Confirm Plan</button>
            </div>

            <div class="workout-details">
                <div class="week-list" v-for="(week, index) in workout" v-bind:key="index">
                    <h5>Week {{ index + 1 }}</h5>
                    <div class="nav nav-tabs nav-fill" id="nav-tab" role="tablist">
                        <a class="nav-link" v-for="(day, day_index) in week" v-bind:key="day_index" data-toggle="tab" :id="`week-${index+1}-day-${day_index + 1}-tab`" :href="`#week-${index+1}-day-${day_index + 1}`" role="tab">{{ `Day ${day_index + 1}` }}</a>
                    </div>
                    <div class="tab-content" id="pills-tabContent">
                        <div class="tab-pane fade workout-content-pane" :id="`week-${index+1}-day-${day_index + 1}`" role="tabpanel" v-for="(day, day_index) in week" v-bind:key="`${day_index}_1`">
                            <div class="rest-day-tab" v-if="day.rest == 1">
                                <img src="../assets/chill.png">
                            </div>
                            <div v-else>
                                <div class="row">
                                    <div class="exercise col-lg-2" v-for="exercise in day.exercises" v-bind:key="exercise[0]">
                                        <div class="exercise--quantity">
                                            <div class="quantity">{{ exercise.reps }}</div>
                                            <div class="steps">{{ exercise.sets }} Sets</div>
                                        </div>
                                        <h5 class="exercise--name">{{ exercise.exercise }}</h5>
                                        <div>Votes: {{ exercise.numberOfVotes }}</div>
                                        <div>Likes: {{ exercise.likes }}</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

        </div>
    </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
    name: 'ViewPlan',
    data() {
        return {
            calculated_data: {},
            workout: [],
        }
    },
    methods: {

        handleConfirmPlan() {

            this.$http.post('/routine/create', {calculated_data: this.calculated_data, workouts: this.workout}).then((response) => {
                console.log(response);
                this.$router.push({name: 'view-routine', params: { routineId: response.data.message["_id"] }});
            }).catch(error => {
                console.log(error);
            });

        }

    },
    mounted() {
        this.calculated_data = this.$route.params.data;
        this.workout = this.$route.params.workout;

        function shuffle(array) {
            var currentIndex = array.length,
                temporaryValue, randomIndex;

            // While there remain elements to shuffle...
            while (0 !== currentIndex) {

                // Pick a remaining element...
                randomIndex = Math.floor(Math.random() * currentIndex);
                currentIndex -= 1;

                // And swap it with the current element.
                temporaryValue = array[currentIndex];
                array[currentIndex] = array[randomIndex];
                array[randomIndex] = temporaryValue;
            }

            return array;
        }

        this.workout.forEach(workout => {

            this.workout.forEach((day: any) => {

                if (day.rest == 0) {

                    day.exercises = shuffle(day.exercises);

                }

            });

        });

        console.log(this.calculated_data, this.workout);

    }
});
</script>

<style lang="scss">
.view-plan {
    margin-top: 10rem;
    .heading {
        font-weight: 500;
        color: black;
    }
}

.calculated-data {
    display: flex;
    margin-top: 3rem;
    .data-item {
        flex: 0 0 20%;
        margin-right: 5rem;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
}

.workout-details {
    margin-top: 3rem;
    margin-bottom: 5rem;
    .week-list {
        margin: 3rem 0 0 0;
    }
    .workout-content-pane {
        padding: 4rem 2rem;
    }
    .nav-tabs {
        border-bottom: 1px solid black;
        margin-top: 2rem;
    }
    .nav-tabs .nav-link {
        border: none;
        color: black;
        font-weight: 400;
        font-size: 1.2rem;
        text-decoration: none;
    }
    .nav-tabs .nav-item.show .nav-link,
    .nav-tabs .nav-link.active {
        color: white;
        background-color: black;
    }
    .rest-day-tab {
        display: flex;
        justify-content: center;
        align-items: center;
        img {
            height: 10rem;
        }
    }
    .exercise {
        display: flex;
        flex-direction: column;
        align-items: center;
        &--quantity {
            height: 7rem;
            width: 7rem;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            margin-bottom: 2rem;
            background-color: #4285F4;
            color: white;
            font-weight: bold;
            border: 2px solid darken($color: #4285F4, $amount: 10%);
            border-radius: 50%;
            font-size: 2rem;
            .steps {
                font-size: 1rem;
            }
        }
        &--name {
            text-align: center;
            font-weight: 400;
            text-transform: capitalize;
        }
    }
}
</style>
