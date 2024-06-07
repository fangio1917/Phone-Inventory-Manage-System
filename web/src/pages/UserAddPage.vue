<template>
  <div class="q-pa-md">
    <div class="login_box column" style="max-width: 300px">
      <p class="text-h5 text-center">添加用户</p>
      <q-input v-model="name" label="用户名" placeholder="请输入用户名"/>
      <q-input v-model="password" label="密码" placeholder="用户密码"/>
      <q-select
                  filled
                  v-model="permission"
                  :options="options"
                  label="Permission"
                  emit-value
                  map-options

      />
      <q-btn color="white" text-color="black" label="添加" @click="add"/>
    </div>
  </div>
</template>

<script setup>
import {ref} from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router'
// 定义组件名称
defineOptions({
  name: 'userAddPage'
});


// 定义响应式数据
const name = ref('');
const password = ref('');
const permission = ref('');
const user_token = window.localStorage.getItem('token')
const options= ['root', 'admin', 'user']

const router = useRouter();

const add = async () => {
   try {
        const response = await axios.post('http://localhost:9000/api/users/add', {
          name: name.value,
          password: password.value,
          permission: permission.value
        },{
          headers: {
            'Authorization': `Bearer ${user_token}`
          }
        })

        if (response.data.success) {
          console.log(response.data.message)
          alert('添加成功')
          await router.push('/users')
        } else {
          alert('Fetching users failed: ' + response.data.message)
        }
      } catch (error) {
        console.error('Error fetching user:', error)
        alert('An error occurred during fetching user')
      }
};
</script>

<style>
.login_box {
  margin-left: 40%;
  margin-top: 10%;
}
</style>
