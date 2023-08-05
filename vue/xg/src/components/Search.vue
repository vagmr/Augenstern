<template>
  <div class="search">
    <p v-color="s">每日一句：{{ sentence }}</p>
    <p>搜索关键字:{{ $route.query.key }}</p>
    <p>搜索结果:</p>
    <ul>
      <li>.............</li>
      <li>.............</li>
      <li>.............</li>
      <li>.............</li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "SearchPage",
  data() {
    return {
      sentence: "",
      s: "red",
    };
  },
  created() {
    new axios({
      url: "http://hmajax.itheima.net/api/ambition",
    })
      .then((res) => (this.sentence = res.data.data))
      .catch((err) => console.log(err));
  },
};
</script>

<style>
.search {
  width: 400px;
  height: 240px;
  padding: 0 20px;
  margin: 0 auto;
  border: 2px solid #c4c7ce;
  border-radius: 5px;
}
</style>