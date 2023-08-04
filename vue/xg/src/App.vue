<template>
  <div>
    <UsersInfo :name="name" />
    <ShopList />
    <!-- <Goods /> -->
    <!-- 不能使用自闭合标签传入插槽 -->
    <ProBar :w="w" id="pro"></ProBar>
    <XH />
    <!-- <BaseIndex /> -->
    <!-- <NewsR /> -->
    <IndexPage />
  </div>
</template>

<script>
// import Goods from "./components/Goods";
import UsersInfo from "./components/UsersInfo";
import ProBar from "./components/ProBar";
import XH from "./components/XhIndex.vue";
// import NewsR from "./components/NewsR";
// import BaseIndex from "./components/事件总线/BaseIndex";
import ShopList from "./components/ShopList.vue";
import IndexPage from "./views/Index.vue";

export default {
  name: "App",
  data() {
    return {
      name: "张三",
      w: 30,
      green: "green",
    };
  },
  components: {
    // Goods,
    UsersInfo,
    ProBar,
    XH,
    // NewsR,
    ShopList,
    IndexPage,
    // BaseIndex,
  },
};
</script>

<style>
#pro {
  position: absolute;
  top: 40px;
  left: 45%;
}
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