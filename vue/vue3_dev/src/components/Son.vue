<script setup>
import { countStore } from '@/store/count.js'
import { useChannelStore } from '@/store/channel.js'
const channel = useChannelStore()
const countStore1 = countStore()
defineOptions({
    name: 'SonCom'
})
</script>
<template>
    <div>
        <h2>这是子组件 --> {{ countStore1.count }} -- {{ countStore1.getCount }}</h2>
        <button @click="countStore1.add">+</button>
        <button @click="channel.getList">-</button>
        <ul>
            <li v-for="el in channel.channelList" :key="el.id">
                {{ el.name }}
            </li>
        </ul>
    </div>
</template>

<style scoped></style>
