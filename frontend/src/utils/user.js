// Only for page setup function
import { ref } from 'vue'
import { getUserInfo, setToken, setUserInfo } from './auth'
const userInfo = ref(getUserInfo()) // Dynamic response object, can be updated at any time
export function useUser() {
  function saveLoginData(data) {
    setToken(data.token)
    setUserInfo(data.user)
    userInfo.value = data.user
  }
  function updateUser(user) {
    setUserInfo(user)
    userInfo.value = data.user
  }
  function reloadUser() {
    userInfo.value = getUserInfo()
  }
  return {
    userInfo,
    saveLoginData,
    updateUser,
    reloadUser
  }
}