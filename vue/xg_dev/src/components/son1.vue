<template>
  <div class="box">
    <h2>Son1 子组件</h2>
    从vuex中获取的值: {{value }} <label></label>
    <br>
    <button @click="vAdd">值 + 1</button>
    <button @click="add5(5)">值 + 5</button>
    <ul>
      <li v-for="(p,index) in filterList" :key="index">
      {{ p }}
      </li>
    </ul>
  </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex'
export default {
  name: 'Son1Com',
  computed: {
    ...mapState(['value']),
    ...mapGetters(['filterList'])
  },
  methods: {
    vAdd () {
      this.$store.state.value++
    },
    add5 (n) {
      this.$store.commit('addVal', n)
    }
  }
}
</script>

<style lang="css" scoped>
.box{
  border: 3px solid #ccc;
  width: 400px;
  padding: 10px;
  margin: 20px;
}
h2 {
  margin-top: 10px;
}
</style>
