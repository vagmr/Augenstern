<script setup>
import ReactiveTest from './components/ReactiveTest.vue'
import SonCom from '@/components/Son.vue'
import { countStore } from '@/store/count.js'
//创建仓库实例
const countStore1 = countStore()
</script>

<template>
  <main class="reactiveTest">
    <h1>根组件 -》 {{ countStore1.count }}</h1>
    <ReactiveTest />
    <SonCom />
  </main>
</template>

<style scoped>
.reactiveTest {
  position: absolute;
  top: 0;
  left: 0;
}
</style>
