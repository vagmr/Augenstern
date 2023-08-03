<template>
  <!-- 输入框 -->
  <header class="header">
    <h1>小黑记事本</h1>
    <!-- 给回车也加上添加事件 -->
    <input
      placeholder="请输入任务"
      class="new-todo"
      v-model="value"
      @keyup.enter="addList"
    />
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
      //添加非空判断
      if (this.value.trim() === "") {
        alert("输入不能为空");
        return;
      }
      //向父组件发送消息
      this.$emit("addInfo", {
        id: this.list.length + 1,
        name: this.value,
        done: false,
        time: new Date().toLocaleString(),
      });
      this.value = "";
    },
  },
};
</script>


