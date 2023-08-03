<template>
  <div>
    <UsersInfo :name="name" />
    <Goods />
    <Goods phoneName="苹果" :price="9999" />
    <ProBar :w="w" />
    <XH />
  </div>
</template>

<script>
import Goods from "./components/Goods";
import UsersInfo from "./components/UsersInfo";
import ProBar from "./components/ProBar";
import XH from "./components/XhIndex.vue";
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
  },
};
</script>

<style>
</style>