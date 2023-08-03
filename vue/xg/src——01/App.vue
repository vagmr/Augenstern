<template>
  <div>
    <img src="./assets/logo.png" alt="logo" />
    <PhoneI></PhoneI>
  </div>
</template>

<script>
//引入组件
import PhoneI from "./components/Ele";

export default {
  name: "App",
  components: {
    PhoneI,
  },
};
</script>

<style>
</style>