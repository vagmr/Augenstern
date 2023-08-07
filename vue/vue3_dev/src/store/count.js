import { defineStore } from "pinia";
import { ref, computed } from "vue"

//定义store
export const countStore = defineStore("count", () => {
    //定义数据
    const count = ref(0)
    //定义getters
    const getCount = computed(() => {
        return count.value + 3
    })
    //定义actions
    const add = () => {
        count.value++
    }
    //定义返回
    return {
        count,
        add,
        getCount
    }
}, {
    persist: {
        key: 'xg-count'
    }                //开启当前模块的持久化
})