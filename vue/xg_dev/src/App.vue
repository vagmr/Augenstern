<template>
  <div class="app">
    <h1>根组件 -- {{title}}</h1>
    <input type="text" :value="value" @input="vChange">
    <Son1Com></Son1Com>
    <hr>
    <Son2Com></Son2Com>
  </div>
</template>

<script>
import Son1Com from '@/components/son1'
import Son2Com from '@/components/son2'
import { mapState } from 'vuex'

export default {
  name: 'App',
  components: { Son1Com, Son2Com },
  methods: {
    vChange (e) {
      this.$store.commit('vChange', +e.target.value)
    }
  },
  computed: {
    ...mapState(['title', 'value'])
  }
}
</script>

<style>
.app{
  width: 800px;
  border: 3px solid #ccc;
  margin-top:30px;
}
</style>
