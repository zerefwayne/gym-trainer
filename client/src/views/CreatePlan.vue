<template>
    <div class="create-plan">
        <div class="create-plan-form">
        <div class="container">
            <h3 class="display-4 heading">Create new fitness plan</h3>
            <div class="form-card">
                <form @submit.prevent="submitForm">
                    <div class="form-group">
                        <label for="inputAge">Age</label>
                        <input type="number" class="form-control" id="inputAge" v-model="formData.age" aria-describedby="emailHelp" placeholder="Enter age">
                    </div>
                    <div class="form-group">
                        <label for="inputWeight">Weight (in kg)</label>
                        <input type="number" class="form-control" id="inputWeight" v-model="formData.weight" aria-describedby="emailHelp" placeholder="Enter weight">
                    </div>
                    <div class="form-group">
                        <label for="inputHeight">Height (in cm)</label>
                        <input type="number" class="form-control" id="inputHeight" v-model="formData.height" aria-describedby="emailHelp" placeholder="Enter height">
                    </div>
                    <div class="form-group">
                        <label for="inputTime">Time you can devote (in minutes)</label>
                        <input type="number" class="form-control" id="inputTime" v-model="formData.time" aria-describedby="emailHelp" placeholder="Enter time">
                    </div>
                    <div class="form-group">
                        <p style="font-size: 1.2rem;">Select the goal you want to achieve:</p>
                    </div>
                    <div class="form-group">
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" name="workoutGoal" v-model="formData.goal" id="checkRipped" value="ripped">
                            <label class="form-check-label" for="checkRipped">Ripped</label>
                        </div>
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" name="workoutGoal" v-model="formData.goal" id="checkFit" value="fit">
                            <label class="form-check-label" for="checkFit">Fit</label>
                        </div>
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" name="workoutGoal" v-model="formData.goal" id="checkSlim" value="slim">
                            <label class="form-check-label" for="checkSlim">Slim</label>
                        </div>
                    </div>
                    <div class="form-group">
                        <p style="font-size: 1.2rem;">Select the body parts you want to focus on:</p>
                    </div>
                    <div class="form-group">
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" v-model="formData.choices" value="chest" id="check1">
                            <label class="form-check-label" style="text-transform: capitalize;" for="check1">
                                        chest
                                    </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" v-model="formData.choices" value="back" id="check2">
                            <label class="form-check-label" style="text-transform: capitalize;" for="check2">
                                        back
                                    </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" v-model="formData.choices" value="shoulders" id="check3">
                            <label class="form-check-label" style="text-transform: capitalize;" for="check3">
                                        shoulders
                                    </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" v-model="formData.choices" value="legs" id="check4">
                            <label class="form-check-label"  style="text-transform: capitalize;"for="check4">
                                        legs
                                    </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" v-model="formData.choices" value="biceps" id="check5">
                            <label class="form-check-label" style="text-transform: capitalize;" for="check5">
                                        biceps
                                    </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" v-model="formData.choices" value="tricep" id="check6">
                            <label class="form-check-label" style="text-transform: capitalize;" for="check6">
                                        tricep
                                    </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" v-model="formData.choices" value="forearms" id="check7">
                            <label class="form-check-label" style="text-transform: capitalize;" for="check7">
                                        forearms
                                    </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" v-model="formData.choices" value="abdomen" id="check8">
                            <label class="form-check-label" style="text-transform: capitalize;" for="check8">
                                        abdomen
                                    </label>
                        </div>
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                </form>
            </div>
        </div>
        </div>
        <div class="create-plan-illustration">
            Helloo
        </div>
    </div>
</template>

<script lang="ts">
import Vue from 'vue';
import axios from 'axios';

export default Vue.extend({
    name: 'CreatePlan',
    props: {

    },
    data() {
        return {
            formData: {
                age: 0,
                weight: 0,
                height: 0,
                time: 0,
                choices: [],
                goal: ""
            }
        }
    },
    methods: {

        async submitForm(event: any) {

            console.log(this.formData);

            console.log("Sending post request!");

            axios.post('http://localhost:5000/api/create_plan', this.formData).then(({data}) => {

                this.$router.push({name: 'view-plan', params: data});

            });


        }

    }
});
</script>

<style lang="scss">
.create-plan {
    height: 100vh;
    width: 100%;

    display: flex;
    flex-direction: row;

    .heading {

        font-weight: 500;
        color: black;

    }


    &-form{


        flex: 0 0 70%;
        padding-left: 5rem;
        display: flex;
        align-items: center;

    }

    &-illustration {

        flex: 1;
        background: url('../assets/create-plan.jpg');
        background-size: cover;
    }

}

.form-card {
    max-width: 50%;
    margin-top: 3rem;
    border-radius: 5px;
}
</style>
