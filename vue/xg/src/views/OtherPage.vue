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
import UsersInfo from "@/components/UsersInfo.vue";
import ProBar from "@/components/ProBar";
import XH from "@/components/XhIndex.vue";
// import NewsR from "./components/NewsR";
// import BaseIndex from "./components/事件总线/BaseIndex";
import ShopList from "@/components/ShopList.vue";
import IndexPage from "@/views/Index.vue";
export default {
  name: "OtherPage",
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

<style scoped>
#pro {
  position: absolute;
  top: 100px;
  left: 45%;
}
</style>