<template>
  <div class="q-pa-md">
    <q-table
      title="users"
      :rows="rows"
      :columns="columns"
      row-key="id"
      :filter="filter"
      binary-state-sort
    >

    <template v-slot:top>
      <q-btn color="primary" :disable="loading" label="增加用户" @click="addRow" />
      <q-space />
      <q-input dense debounce="300" color="primary" v-model="filter">
        <template v-slot:append>
          <q-icon name="search" />
        </template>
      </q-input>
    </template>

      <template v-slot:bottom>
      <q-btn class="q-ml-sm" color="primary" :disable="loading" label="删除用户" @click="removeRow" />
      <q-btn class="q-ml-sm" color="primary" :disable="loading" label="修改用户" @click="modifyRow" />
      </template>

    <template v-slot:body="props">
      <q-tr :props="props">
        <q-td key="name" :props="props">
          {{ props.row.name }}
          <q-popup-edit v-model="props.row.name" title="Update name" buttons v-slot="scope">
            <q-input v-model="scope.value" dense autofocus counter />
          </q-popup-edit>
        </q-td>
        <q-td key="password" :props="props">
          {{ props.row.password }}
          <q-popup-edit v-model="props.row.password" title="Update calories" buttons v-slot="scope">
            <q-input v-model="scope.value" dense autofocus />
          </q-popup-edit>
        </q-td>
        <q-td key="permission" :props="props">
          {{ props.row.permission }}
          <q-popup-edit v-model="props.row.permission" title="Update protein" buttons v-slot="scope">
             <q-select
                filled
                v-model="scope.value"
                :options="options"
                label="Permission"
                emit-value
                map-options
                dense
                autofocus
              />
          </q-popup-edit>
        </q-td>
        <q-td key="id" :props="props">{{ props.row.id }}</q-td>
      </q-tr>
    </template>

    </q-table>
  </div>
</template>

<script>
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

export default {
  setup() {
    const loading = ref(false)
    const filter = ref('')
    const rows = ref([])
    const selected = ref([])

    const options= ['root', 'admin', 'user']

    const columns = [
      {
        name: 'name',
        required: true,
        label: '姓名',
        align: 'center',
        field: row => row.name,
        format: val => `${val}`,
        sortable: true
      },
      {
        name: 'password',
        required: false,
        label: '密码',
        align: 'center',
        field: row => row.password,
        format: val => `${val}`,
        sortable: true
      },
      {
        name: 'permission',
        required: true,
        label: '权限',
        align: 'center',
        field: row => row.permission,
        format: val => `${val}`,
        sortable: true
      },
      {
        name: 'id',
        required: true,
        label: 'ID',
        align: 'center',
        field: 'id',
        sortable: true
      }
    ]

    const user_token = window.localStorage.getItem('token')

    const getUsers = async () => {
      console.log('Fetching users...')
      try {
        const response = await axios.get('http://localhost:9000/api/users/query', {
          headers: {
            'Authorization': `Bearer ${user_token}`
          }
        })

        if (response.data.success) {
          console.log(response.data)
          rows.value = response.data.data // Assign data directly to rows
        } else {
          alert('Fetching users failed: ' + response.data.message)
        }
      } catch (error) {
        console.error('Error fetching users:', error)
        alert('An error occurred during fetching users')
      }
    }

    onMounted(() => {
      getUsers()
    })

    const router = useRouter()

    const addRow = () => {
      router.push('/users/add')
    }

    const removeRow = () => {
      router.push('/users/delete')
    }

    const modifyRow = async () => {
      try {
        let data= JSON.parse(JSON.stringify(rows.value))
        const response = await axios.put('http://localhost:9000/api/users/update', {
          data
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

    return {
      selected,
      columns,
      rows,
      loading,
      filter,
      options,
      addRow,
      removeRow,
      modifyRow
    }
  }
}
</script>
