<template>
  <div class="home">
    <div class="logo-box"></div>
    <div class="search-box">
      <input type="text" v-model="sValue" />
      <button @click="goSearch">搜索一下</button>
    </div>
    <div class="hot-link">
      热门搜索：
      <router-link to="/search?key=c++">c++</router-link>
      <router-link to="/search?key=java">java</router-link>
      <router-link to="/search?key=Rust">Rust</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomePage",
  data() {
    return {
      sValue: "",
    };
  },
  methods: {
    goSearch() {
      this.$router.push({
        path: "/search",
        query: {
          key: this.sValue,
        },
      });
    },
  },
};
</script>

<style>
.logo-box {
  height: 150px;
  background: url("@/assets/logo.png") no-repeat center;
  background-size: 150px 100px;
  margin-top: 50px;
}
.search-box {
  display: flex;
  justify-content: center;
}
.search-box input {
  width: 400px;
  height: 30px;
  line-height: 30px;
  border: 2px solid #c4c7ce;
  border-radius: 4px 0 0 4px;
  outline: none;
}
.search-box input:focus {
  border: 2px solid #ad2a26;
}
.search-box button {
  width: 100px;
  height: 36px;
  border: none;
  background-color: #ad2a26;
  color: #fff;
  position: relative;
  left: -2px;
  border-radius: 0 4px 4px 0;
}
.hot-link {
  width: 508px;
  height: 60px;
  line-height: 60px;
  margin: 0 auto;
}
.hot-link a {
  margin: 0 5px;
}
</style>