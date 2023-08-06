import axios from 'axios'
export default {
  namespaced: true,
  state () {
    return {
      list: []
    }
  },
  mutations: {
    updateList (state, newList) {
      state.list = newList
    },
    /* 在JavaScript中，对象是引用类型。当我们将一个对象赋值给一个变量时，实际上是将对象的引用赋值给了变量，而不是复制整个对象。所以当你通过state.list.find找到了要修改的商品对象并将其赋值给goods变量时，goods实际上是指向state.list数组中对应对象的引用。
    因此，当你修改goods对象的属性时，实际上是直接修改了state.list数组中对应对象的属性。因为它们指向的是同一个内存地址，所以任何对goods对象的修改都会影响到state.list数组中对应对象的值。
    这也是为什么在updateCount方法中直接修改goods.count的值，页面会随之更新的原因。因为Vue.js会检测到state.list数组发生了变化，从而重新渲染相关的组件，使页面上显示的商品数量也随之更新。 */
    updateCount (state, obj) {
      const goods = state.list.find(el => el.id === obj.id)
      goods.count = obj.count
    }
  },
  getters: {
    // 商品总数
    total (state) {
      return state.list.reduce((sum, item) => sum + item.count, 0)
    },
    // 商品总价
    totalPrice (state) {
      return state.list.reduce((sum, item) => sum + item.count * item.price, 0)
    }
  },
  actions: {
    async getList (context) {
      const res = await axios.get('http://localhost:3000/cart')
      context.commit('updateList', res.data)
    },
    async updateListAsync (cxk, obj) {
      await axios.patch(`http://localhost:3000/cart/${obj.id}`, {
        count: obj.count
      })
      cxk.commit('updateCount', obj)
    }
  }
}
