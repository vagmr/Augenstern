<template>
  <div>
    <div class="footer_wrap">
      <router-link to="/home">首页</router-link>
      <router-link to="/other">其他页面</router-link>
      <router-link to="/mjindex">面经首页</router-link>
    </div>
    <div class="top">
      <!-- 路由出口 → 匹配的组件所展示的位置 -->
      <keep-alive :include="['LayoutPage']">
        <router-view></router-view>
      </keep-alive>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {};
  },
  components: {},
};
</script>

<style>
.loading::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #fff;
  background: url(./assets/loading.gif) no-repeat center center;
}
</style>

<style scoped>
body {
  margin: 0;
  padding: 0;
}
.footer_wrap {
  position: relative;
  left: 0;
  top: 0;
  display: flex;
  width: 100%;
  text-align: center;
  background-color: #333;
  color: #ccc;
}
.footer_wrap a {
  flex: 1;
  text-decoration: none;
  padding: 20px 0;
  line-height: 20px;
  background-color: #333;
  color: #ccc;
  border: 1px solid black;
}
.footer_wrap .router-link-active {
  background-color: aqua;
}
.footer_wrap a:hover {
  background-color: #555;
}
</style>