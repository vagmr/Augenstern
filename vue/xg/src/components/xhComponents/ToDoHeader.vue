<template>
  <!-- 输入框 -->
  <header class="header">
    <h1>小黑记事本</h1>
    <input placeholder="请输入任务" class="new-todo" v-model="value" />
    <button class="add" @click="addList">添加任务</button>
  </header>
</template>

<script>
export default {
  name: "ToDoHeader",
  data() {
    return {
      value: "",
    };
  },
  props: {
    list: Array,
  },
  methods: {
    addList() {
      //向父组件发送消息
      this.$emit("addInfo", {
        id: this.list.length + 1,
        name: this.value,
        done: false,
      });
      this.value = "";
    },
  },
};
</script>


