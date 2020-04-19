<template>
    <nav  class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
        <a class="navbar-brand" href="#">
            <img src="../assets/text_logo.png" height="35px">
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <router-link :to="{name: 'profile'}" tag="li" class="nav-item" active-class="active">
                    <a class="nav-link" href="#">Profile</a>
                </router-link>
                <router-link :to="{name: 'create-plan'}" tag="li" class="nav-item" exact-active-class="active" >
                    <a class="nav-link" href="#">Create Plan</a>
                </router-link>
                <li class="nav-item" v-if="user !== null">
                    <a class="nav-link" style="" href="#" @click="handleLogout">Logout</a>
                </li>
            </ul>
        </div>
    </nav>
</template>

<script lang="ts">
import Vue from 'vue';
import { mapState, mapGetters } from 'vuex';

export default Vue.extend({
    name: 'Navbar',
    props: {

    },
    data() {
        return {
        }
    },
    methods: {

        handleLogout() {
            this.$http.get('/auth/logout').then((response: any) => {

                console.log("Successfully logged out!", response.data);

                this.$store.dispatch('initApp', null).then(() => {
                    this.$router.push({name: 'login'});
                });

            }).catch(error => {
                console.log(error);
            });
        },
    },
    computed: mapState(['user'])
});
</script>

<style lang="scss">

    nav.navbar{

        background-color: #000000!important;
        display: flex;
        align-items: center;


        .navbar-brand {

            font-weight: normal;
            color: white;
            text-decoration: none;
        }

        .nav-item {
            font-size: 1.2rem;
        }

    }

</style>
