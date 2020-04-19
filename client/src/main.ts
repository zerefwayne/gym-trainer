import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import VuePageTransition from 'vue-page-transition';
import axios from 'axios';

const axiosBaseConfig = axios.create({
  baseURL: 'http://localhost:3000',
  withCredentials: true,
});

Vue.prototype.$http = axiosBaseConfig;

Vue.config.productionTip = false;
Vue.use(VuePageTransition);

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
