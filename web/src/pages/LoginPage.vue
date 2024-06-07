<template>
  <div class="q-pa-md">
    <div class="login_box column" style="max-width: 400px">
      <p class="text-h5 text-center">登录</p>
      <q-input v-model="ph" label="用户名" placeholder="请输入用户名" hint="username" />
      <q-input v-model="password" label="密码" filled type="password" placeholder="请输入密码" hint="Password" />
      <q-btn color="white" text-color="black" label="登陆" @click="login" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
// 定义组件名称
defineOptions({
  name: 'LoginPage'
});

const ph = ref('');
const password = ref('');
const router = useRouter();

const login = async () => {
  console.log('Login button clicked');
  try {
    const response = await axios.post('http://localhost:9000/back-end/login', {
      name: ph.value,
      password: password.value,
    })
    if (response.data.success) {
      alert('Login successful');
      // 在这里处理登录成功后的逻辑，例如跳转到首页
      window.localStorage.setItem("token", response.data.Authorization)
      await router.push('/index');
    } else {
      alert('Login failed: ' + response.data.message);
    }
  } catch (error) {
    console.error('Error logging in:', error);
    alert('An error occurred during login');
  }
};
</script>

<style>
.login_box {
  margin-left: 40%;
  margin-top: 10%;
}
</style>
