<template>
  <div class="login-container">
    <div class="login-box">
      <h1 style="font-size: 28px">Laboratory Reservation System</h1>
      <div style="margin-top: 5px; margin-bottom: 30px">
        Agent-Based Intelligent Reservation System
      </div>

      <el-form :model="form" label-width="auto" style="max-width: 600px">
        <el-form-item>
          <el-input
            size="large"
            v-model="form.username"
            placeholder="Please enter your account"
            :prefix-icon="User"
          />
        </el-form-item>
        <el-form-item>
          <el-input
            type="password"
            size="large"
            v-model="form.password"
            placeholder="Please enter your password"
            :prefix-icon="Lock"
            show-password
          />
        </el-form-item>
        <div>
          <el-button
            size="large"
            type="primary"
            style="width: 100%"
            @click="login"
            :loading="loadingValue"
            >Log In</el-button
          >
          <div style="text-align: right; margin-top: 20px">
            Don't have an account? Please
            <a style="color: var(--el-color-primary)" href="/register">Register</a>
          </div>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { User, Lock } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'
import router from '@/router'

const form = reactive({
  username: '',
  password: ''
})

const loadingValue = ref(false)

const login = () => {
  loadingValue.value = true
  setTimeout(() => {
    loadingValue.value = false
    ElMessage.success('Login successful')
    router.push('/manager/home')
  }, 2000)
}
</script>

<style scoped>
.login-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
.login-box {
  width: 380px;
  border-radius: 8px;
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.1);
  padding: 30px;
  text-align: center;
  background-color: white;
}
</style>
