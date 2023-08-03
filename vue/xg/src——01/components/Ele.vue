<template>
  <div class="demo">
    <h1>手机品牌： {{ phoneName }}</h1>
    <h2>手机价格: {{ price }}</h2>
    <h2>手机核心: {{ phonecore }}</h2>
    <button @click="show"></button>
  </div>
</template>
<script>
//组件交互相关的代码
export default {
  name: "PhoneI",
  data() {
    return {
      phoneName: "华为",
      price: 4999,
      phonecore: "麒麟990",
    };
  },
  methods: {
    show() {
      alert("this is phone");
    },
  },
};
</script>
<style>
.demo {
  text-align: center;
  font-family: "Franklin Gothic Medium";
  font-size: 18px;
  font-weight: 400;
  color: #2c3e50;
  background-color: azure;
}
</style>