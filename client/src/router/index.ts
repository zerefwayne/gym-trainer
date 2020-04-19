import Vue from 'vue';
import VueRouter from 'vue-router';
import CreatePlan from '../views/CreatePlan.vue';
import ViewPlan from '../views/ViewPlan.vue';
import ViewRoutine from '../views/ViewRoutine.vue';
import Profile from '../views/Profile.vue';
import Login from '../views/Login.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'create-plan',
    component: CreatePlan,
  },
  {
    path: '/plan',
    name: 'view-plan',
    component: ViewPlan,
  }, {
    path: '/login',
    name: 'login',
    component: Login,
    meta: { hideNavigation: true },
  }, {
    path: '/routine',
    name: 'view-routine',
    component: ViewRoutine,
  }, {
    path: '/profile',
    name: 'profile',
    component: Profile,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
