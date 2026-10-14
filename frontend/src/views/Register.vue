<template>
  <div class="register-container">
    <div class="register-box">
      <h1 style="font-size: 24px; margin-bottom: 30px">
        Welcome to Register for the Laboratory Reservation System
      </h1>

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
        <el-form-item>
          <el-input
            type="password"
            size="large"
            v-model="form.confirmPassword"
            placeholder="Please confirm your password"
            :prefix-icon="Lock"
            show-password
          />
        </el-form-item>
        <div>
          <el-button size="large" type="primary" style="width: 100%">Register</el-button>
          <div style="text-align: right; margin-top: 20px">
            Already have an account? Please
            <a style="color: var(--el-color-primary)" href="/login">Log In</a>
          </div>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue'
import { User, Lock } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'

const form = reactive({
  username: '',
  password: '',
  confirmPassword: ''
})
</script>

<style scoped>
.register-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
.register-box {
  width: 380px;
  border-radius: 8px;
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.1);
  padding: 30px;
  text-align: center;
  background-color: white;
}
</style>
