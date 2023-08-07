<script>

</script>
<script setup>
import { reactive } from 'vue'
//使用ref将简单数据类型转成响应式
import { ref } from 'vue'
import { computed } from 'vue'
import { watch, nextTick } from 'vue';

defineOptions({
    name: 'ReactiveTest',
})
const state = reactive({
    name: 'xg',
    count: 100
})
const rCount = ref(100)
const list = ref([1, 23, 4, 5, 6, 52, 44, 55, 52, 9, 67, 102])
const min = ref(30)
const ipt = ref(null)

//vue3中的计算属性
const comCount = computed(() => {
    return state.count * 4
})
const comList = computed(() => {
    return list.value.filter(el => el > (min.value || 23))
})
const usersInfo = reactive({
    name: 'xg',
    score: 100,
    age: 20,
    sex: '男'
})
const usersInfo2 = ref({
    name: 'xg',
    score: 100,
    age: 20,
    sex: '男'
})

//修改usersInfo的数据
const changeUsersInfo = () => {
    usersInfo.name = '地方'
    usersInfo.score = 200
}
const changeUsersInfo2 = () => {
    usersInfo2.value.score++
}
const changeCount = () => {
    state.count++
}
watch(min, () => {
    comList.value
})
watch(usersInfo2, (newvalue) => {
    console.log(newvalue)
}, {
    deep: true
})
//通过async异步加上nextTick实现聚焦
const focusI = async () => {
    await nextTick()
    ipt.value.focus()
}
</script>
<template>
    <main>
        <div>{{ state.count }}
            <span>简单数据类型转成响应式 => {{ rCount }}</span>
            <span>计算属性 => {{ comCount }}</span>
            <input type="text" v-model="min" ref="ipt">
            <p>计算属性list大于23 => {{ comList }}</p>
        </div>
        <button @click="changeCount">让数字加1</button>
        <button @click="changeUsersInfo">修改usersInfo的数据</button>
        <button @click="changeUsersInfo2">修改usersInfo2的数据</button>
        <button @click="focusI">点击让输入框聚焦</button>
    </main>
</template>

<style scoped>
main {
    width: 400px;
    height: 200px;
    background-color: aqua;
    text-align: center;
}
</style>