import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: null,
  },
  mutations: {
    init_app(state, user) {
      state.user = user;
    },
  },
  actions: {
    initApp({ commit }, user) {
      commit('init_app', user);
    },
  },
  getters: {
    isAuthenticated(state) {
      return state.user !== null;
    },
    getUser(state) {
      return state.user;
    }
  },
});
