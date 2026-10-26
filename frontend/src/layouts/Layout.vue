<template>
  <div>
    <el-container style="min-height: 100vh">
      <el-header
        style="
          display: flex;
          align-items: center;
          border-bottom: 1px solid #ddd;
          background-color: #fff;
        "
      >
        <div
          style="flex: 1; display: flex; align-items: center; font-size: 24px; font-weight: bold"
        >
          <img style="width: 40px" src="@/assets/imgs/logo.png" alt="" />
          <div style="margin-left: 5px">Intelligent Laboratory Reservation System</div>
        </div>

        <!-- 用户信息下拉菜单 -->
        <el-dropdown>
          <div style="display: flex; align-items: center; cursor: pointer; outline: none">
            <img
              src="@/assets/imgs/logo.png"
              alt=""
              style="width: 30px; border-radius: 50%"
            />
            <div style="margin-left: 3px">Administrator</div>
            <el-icon style="margin-left: 5px"><ArrowDown /></el-icon>
          </div>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item @click="handleLogout">Logout</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </el-header>

      <el-container>
        <el-aside width="250px">
          <el-menu router style="height: 100%" default-active="/manager/home">
            <el-menu-item index="/manager/home">
              <el-icon><icon-menu /></el-icon>
              System Home
            </el-menu-item>
            <el-menu-item index="/manager/lab">
              <el-icon><House /></el-icon>
              Laboratory Management
            </el-menu-item>
            <el-menu-item index="/manager/equ">
              <el-icon><Setting /></el-icon>
              Equipment List Management
            </el-menu-item>
            <el-menu-item index="/manager/user">
              <el-icon><User /></el-icon>
              User Management
            </el-menu-item>
          </el-menu>
        </el-aside>
        <el-main>
          <router-view />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script setup>
import router from '@/router'
import { Menu as IconMenu, House, Setting, User, ArrowDown } from '@element-plus/icons-vue'
import { logout } from '@/utils/auth.js'

const handleLogout = () => {
  logout()
  router.push('/login')
}
</script>