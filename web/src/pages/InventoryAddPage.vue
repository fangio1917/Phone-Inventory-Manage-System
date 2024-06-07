<template>
  <div class="q-pa-md">
    <div class="login_box column" style="max-width: 300px">
      <p class="text-h5 text-center">添加库存</p>
      <q-input v-model="phone" label="手机" placeholder="请输入手机名"/>
       <q-input v-model="manufacturer" label="生产商" placeholder="请输入生产商名"/>
       <q-input v-model="count" type="number" label="数量" placeholder="请输入库存数量"/>
       <q-input v-model="price" type="number" label="价格" placeholder="请输入价格"/>
       <q-input v-model="local" label="地点" placeholder="请输入存放地点"/>

       <q-input filled v-model="date" label="入库时间">
          <template v-slot:prepend>
            <q-icon name="event" class="cursor-pointer">
              <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                <q-date v-model="date" mask="YYYY-MM-DD HH:mm">
                  <div class="row items-center justify-end">
                    <q-btn v-close-popup label="Close" color="primary" flat />
                  </div>
                </q-date>
              </q-popup-proxy>
            </q-icon>
          </template>

          <template v-slot:append>
            <q-icon name="access_time" class="cursor-pointer">
              <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                <q-time v-model="date" mask="YYYY-MM-DD HH:mm" format24h>
                  <div class="row items-center justify-end">
                    <q-btn v-close-popup label="Close" color="primary" flat />
                  </div>
                </q-time>
              </q-popup-proxy>
            </q-icon>
          </template>
      </q-input>

      <q-btn color="white" text-color="black" label="添加" @click="add" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router'
// 定义组件名称
defineOptions({
  name: 'InventoryAddPage'
});

// 定义响应式数据
const phone = ref('');
const manufacturer = ref('');
const count = ref();
const local = ref();
const price = ref('');
const date = ref('2002-12-13 13:00');
const user_token = window.localStorage.getItem('token')
const router = useRouter()

const add = async () => {

  try {
        const response = await axios.post('http://localhost:9000/api/inventory/add', {
          phone: phone.value,
          manufacturer: manufacturer.value,
          count: count.value,
          local: local.value,
          price: price.value,
          date: date.value,
        },{
          headers: {
            'Authorization': `Bearer ${user_token}`
          }
        })

        if (response.data.success) {
          console.log(response.data.message)
          alert('添加成功')
          await router.push('/inventory')
        } else {
          alert('Fetching inventory failed: ' + response.data.message)
        }
      } catch (error) {
        console.error('Error fetching inventory:', error)
        alert('An error occurred during fetching inventory')
      }
};
</script>

<style>
.login_box {
  margin-left: 40%;
  margin-top: 10%;
}
</style>
