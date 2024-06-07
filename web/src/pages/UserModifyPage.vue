<template>
  <div class="q-pa-md">
    <div class="login_box column" style="max-width: 300px">
      <p class="text-h5 text-center">修改用户</p>
      <q-input v-model="id" label="用户编号" placeholder="请输入用户编号"/>
      <q-input v-model="name" label="用户名" placeholder="请输入用户名"/>
      <q-input v-model="password" label="密码" placeholder="用户密码"/>
      <q-input v-model="permission" label="用户权限" placeholder="1:root; 10:admin; 100:user"/>
      <q-btn color="white" text-color="black" label="修改" @click="modify"/>
    </div>
  </div>
</template>

<script setup>
import {ref} from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router'
// 定义组件名称
defineOptions({
  name: 'SongAddPage'
});


// 定义响应式数据
const id = ref('');
const name = ref(null);
const password = ref(null);
const permission = ref(null);
const user_token = window.localStorage.getItem('token');

const router = useRouter();

const modify = async () => {
   try {
    const response = await axios.put('http://localhost:9000/api/users/update', {
      id: Number(id.value),
      name: name.value,
      password: password.value,
      permission: Number(permission.value)
    }, {
      headers: {
        'Authorization': `Bearer ${user_token}`
      }
    })

    if (response.data.success) {
      console.log(response.data.message)
      alert('修改成功')
      await router.push('/users')
    } else {
      alert('modify users failed: ' + response.data.message)
    }
  } catch (error) {
    console.error('Error modify user:', error)
    alert('An error occurred during modify song')
  }
};
</script>

<style>
.login_box {
  margin-left: 40%;
  margin-top: 10%;
}
</style>
