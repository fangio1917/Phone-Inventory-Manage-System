<template>
  <div class="q-pa-md">
    <q-table
      title="inventory"
      :rows="rows"
      :columns="columns"
      row-key="id"
      :filter="filter"
      binary-state-sort
    >

    <template v-slot:top>
      <q-btn color="primary" :disable="loading" label="增加库存" @click="addRow" />
      <q-space />
      <q-input dense debounce="300" color="primary" v-model="filter">
        <template v-slot:append>
          <q-icon name="search" />
        </template>
      </q-input>
    </template>

      <template v-slot:bottom>
      <q-btn class="q-ml-sm" color="primary" :disable="loading" label="删除库存" @click="removeRow" />
      <q-btn class="q-ml-sm" color="primary" :disable="loading" label="修改库存" @click="modifyRow" />
      </template>

    <template v-slot:body="props">
      <q-tr :props="props">

        <q-td key="phone" :props="props">
          {{ props.row.phone }}
          <q-popup-edit v-model="props.row.phone" title="Update phone name" buttons v-slot="scope">
            <q-input v-model="scope.value" dense autofocus counter />
          </q-popup-edit>
        </q-td>

        <q-td key="manufacturer" :props="props">
          {{ props.row.manufacturer }}
          <q-popup-edit v-model="props.row.manufacturer" title="Update manufacturer" buttons v-slot="scope">
            <q-input v-model="scope.value" dense autofocus counter />
          </q-popup-edit>
        </q-td>

        <q-td key="count" :props="props">
          {{ props.row.count }}
          <q-popup-edit  v-model="props.row.count" title="Update count" buttons v-slot="scope">
            <q-input v-model="scope.value" type="number" dense autofocus />
          </q-popup-edit>
        </q-td>

         <q-td key="local" :props="props">
          {{ props.row.local }}
          <q-popup-edit v-model="props.row.local" title="Update local" buttons v-slot="scope">
            <q-input v-model="scope.value" dense autofocus />
          </q-popup-edit>
        </q-td>

         <q-td key="date" :props="props">
          {{ props.row.date }}
          <q-popup-edit v-model="props.row.date" title="Update date" buttons v-slot="scope">
              <q-input filled v-model="scope.value">
                <template v-slot:prepend>
                  <q-icon name="event" class="cursor-pointer">
                    <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                      <q-date v-model="scope.value" mask="YYYY-MM-DD HH:mm">
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
                      <q-time v-model="scope.value" mask="YYYY-MM-DD HH:mm" format24h>
                        <div class="row items-center justify-end">
                          <q-btn v-close-popup label="Close" color="primary" flat />
                        </div>
                      </q-time>
                    </q-popup-proxy>
                  </q-icon>
                </template>
            </q-input>
          </q-popup-edit>
        </q-td>


        <q-td key="price" :props="props">
          {{ props.row.price }}
          <q-popup-edit v-model="props.row.price" title="Update price" buttons v-slot="scope">
            <q-input type="number" v-model="scope.value" dense autofocus />
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

    const columns = [
      {
        name: 'phone',
        required: true,
        label: '手机',
        align: 'center',
        field: row => row.phone,
        format: val => `${val}`,
        sortable: true
      },
      {
        name: 'manufacturer',
        required: true,
        label: '制造商',
        align: 'center',
        field: row => row.manufacturer,
        format: val => `${val}`,
        sortable: true
      },
      {
        name: 'count',
        required: true,
        label: '数量',
        align: 'center',
        field:  'count',
        sortable: true
      },
      {
        name: 'local',
        required: true,
        label: '地址',
        align: 'center',
        field: row => row.local,
        format: val => `${val}`,
        sortable: true
      },
      {
        name: 'date',
        required: true,
        label: '入库日期',
        align: 'center',
        field: row => row.date,
        format: val => `${val}`,
        sortable: true
      },
      {
        name: 'price',
        required: true,
        label: '价格',
        align: 'center',
        field: 'price',
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

    const getInventories = async () => {
      console.log('Fetching users...')
      try {
        const response = await axios.get('http://localhost:9000/api/inventory/query', {
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
      getInventories()
    })

    const router = useRouter()

    const addRow = () => {
      router.push('/inventory/add')
    }

    const removeRow = () => {
      router.push('/inventory/delete')
    }

    const modifyRow = async () => {
      try {
        let data = JSON.parse(JSON.stringify(rows.value))
        const response = await axios.put('http://localhost:9000/api/inventory/update', {
          data
        }, {
          headers: {
            'Authorization': `Bearer ${user_token}`
          }
        })

        if (response.data.success) {
          console.log(response.data.message)
          alert('修改成功')
          await router.push('/inventory')
        } else {
          alert('modify users failed: ' + response.data.message)
        }
      } catch (error) {
        console.error('Error modify user:', error)
        alert('An error occurred during modify song')
      }
    };

    return {
      columns,
      rows,
      loading,
      filter,
      addRow,
      removeRow,
      modifyRow
    }
  }
}
</script>
