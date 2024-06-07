<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title>
          手机库存管理系统
        </q-toolbar-title>

        <div>Quasar v{{ $q.version }}</div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
    >
      <q-list>
        <q-item-label
          header
        >
          导航跳转
        </q-item-label>

        <EssentialLink
          v-for="link in linksList"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref } from 'vue'
import EssentialLink from 'components/EssentialLink.vue'

defineOptions({
  name: 'MainLayout'
})

const linksList = [
  {
    title: '首页',
    caption: '展示平台信息',
    icon: 'home',
    link: 'http://localhost:9000/#/index'
  },
  {
    title: '库存管理',
    caption: '管理您的库存',
    icon: 'note',
    link: 'http://localhost:9000/#/songs'
  },
  {
    title: '管理员管理',
    caption: '管理此平台的人员',
    icon: 'people',
    link: "http://localhost:9000/#/inventory"
  },
  {
    title: 'Code',
    caption: '项目开源，托管至github',
    icon: 'code',
    link: "https://github.com/fangio1917/Phone-Inventory-Manage-System"
  },
  {
    title: '退出',
    caption: '退出当前账号',
    icon: 'logout',
    link: 'http://localhost:9000/'
  }
]

const leftDrawerOpen = ref(false)

function toggleLeftDrawer () {
  leftDrawerOpen.value = !leftDrawerOpen.value
}
</script>
