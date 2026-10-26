import axios from 'axios'
import { getToken, logout } from './auth'
import { ElMessage } from 'element-plus'
import router from '@/router'

// console.log('VITE_API_BASE_URL:', import.meta.env.VITE_API_BASE_URL)

const service = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: 30000 //30s
})

// Request interceptor config
service.interceptors.request.use(
  (config) => {
    const token = getToken()
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (err) => Promise.reject(err)
)

// Response interceptor config
service.interceptors.response.use(
  (res) => {
    const data = res.data
      // console.log('res', res)
    if (data.code !== 200) {
      ElMessage.error(data.message || 'Request failed')
      if (data.code === 401) {
        logout()
        router.push('/login')
        return Promise.reject(data)
      }
    }
    return data
  },
  (err) => {
    if (err.response) {
      const httpStatusCode = err.response.status
      if (httpStatusCode === 401) {
        ElMessage.error('Your login session has expired. Please log in again')
        logout()
        router.push('/login')
      } else {
        ElMessage.error(err.response.data?.message || 'Request failed')
      }
    } else {
      // Backend is not started or network error
      ElMessage.error('Network error. Please check the backend service')
    }
    return Promise.reject(err)
  }
)

export default service