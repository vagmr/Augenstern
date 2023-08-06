import Vue from 'vue'
import Vuex from 'vuex'
import uers from '@/store/modules/uers'

Vue.use(Vuex)
// 创建仓库
const store = new Vuex.Store({
  // 严格模式
  strict: false,
  state: {
    title: 'vuex使用',
    value: 0,
    list: [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10]
  },
  getters: {
    filterList (state) {
      return state.list.filter(el => el > 5)
    }
  },
  mutations: {
    addVal (state, n) {
      state.value += n
    },
    vChange (state, val) {
      state.value = val
    }
  },
  // actions处理异步,actions: {
  actions: {
    addValAsync (ck, n) {
      setTimeout(() => {
        ck.commit('addVal', n)
      }, 1000)
    }
  },
  modules: {
    uers
  }
})
export default store
