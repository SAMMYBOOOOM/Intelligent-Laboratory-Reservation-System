<template>
  <div>Welcome: {{ userInfo?.username }}</div>
</template>

<script setup>
import { useUser } from '@/utils/user'
const { userInfo } = useUser()
</script>
