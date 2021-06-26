import { createStore } from 'vuex'
import { getAPI } from '../axios-api'

export default createStore({
  state: {
    accessToken:null,
    refreshToken:null,
    APIData: ''
  },
  mutations: {
    updateStore (state, {access, refresh}) {
      state.accessToken = access,
      state.refreshToken = refresh
    }
  },
  actions: {
    userLogin (context, usercredentials) {
      return new Promise ((resolve, reject) => {
        getAPI.post('api/token/', {
          username: usercredentials.username,
          password: usercredentials.password
        })
        .then(response => {
          context.commit('updateStore', {access: response.data.access, refresh: response.data.refresh})
          resolve()
        })
        .catch(err => {
          reject(err)
        })
      })
    }
  },
  modules: {
  }
})
