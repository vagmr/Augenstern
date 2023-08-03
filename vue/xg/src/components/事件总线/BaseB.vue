<template>
  <div class="base-b">
    <div>我是B组件（发布方）</div>
    <button @click="sendMsgFn">发送消息</button>
  </div>
</template>

<script>
import Bus from "../../utils/EventBus";

export default {
  name: "BB",
  methods: {
    sendMsgFn() {
      Bus.$emit("sendMsg", "我是B组件发送的消息");
    },
  },
};
</script>

<style scoped>
.base-b {
  width: 200px;
  height: 200px;
  border: 3px solid #000;
  border-radius: 3px;
  margin: 10px;
}
button {
  padding: 10px;
  background-color: royalblue;
}
</style>