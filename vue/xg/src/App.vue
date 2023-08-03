<template>
  <div>
    <UsersInfo :name="name" />
    <Goods />
    <Goods phoneName="苹果" :price="9999" />
    <ProBar :w="w" />
    <XH />
    <BaseIndex />
  </div>
</template>

<script>
import Goods from "./components/Goods";
import UsersInfo from "./components/UsersInfo";
import ProBar from "./components/ProBar";
import XH from "./components/XhIndex.vue";
import BaseIndex from "./components/事件总线/BaseIndex";

export default {
  name: "App",
  data() {
    return {
      name: "张三",
      w: 30,
    };
  },
  components: {
    Goods,
    UsersInfo,
    ProBar,
    XH,
    BaseIndex,
  },
};
</script>

<style>
</style>