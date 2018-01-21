import axios from 'axios'

axios.defaults.baseURL = 'http://api.teamsportapp.com/v1/'
axios.interceptors.request.use(config => {
  // if (store.getters.currentUser.token) {
  //   config.headers.Authorization = 'Token 94ccb42aebecbd6b486df435bbbb213d01c35016'
  // }
  return config
}, err => {
  return Promise.reject(err)
})
export default axios
