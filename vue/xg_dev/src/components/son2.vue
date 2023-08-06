<template>
  <div class="box">
    <h2>Son2 子组件</h2>
    从vuex中获取的值: {{ $store.state.value }}<label></label>
    <br />
    <button @click="vSub">值 - 1</button>
    <button @click="comSub(15)">值 + 15</button>
    <button @click="addValAsync(30)">值 + 30</button>
    <!-- 原生访问模块中的state -->
    <div>{{ $store.state.uers.userInfo.age }}</div>
    <!-- 通过辅助函数访问  -->
    <div>{{ score }}</div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  name: 'Son2Com',
  computed: {
    ...mapState('uers', ['score'])
  },
  methods: {
    vSub () {
      this.$store.state.value--
    },
    comSub (n) {
      this.$store.dispatch('addValAsync', n)
    },
    ...mapActions(['addValAsync'])
  }
}
</script>

<style lang="css" scoped>
.box {
  border: 3px solid #ccc;
  width: 400px;
  padding: 10px;
  margin: 20px;
}
h2 {
  margin-top: 10px;
}
</style>
