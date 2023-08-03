<template>
  <!-- 统计和清空 -->
  <footer class="footer">
    <!-- 统计 -->
    <span class="todo-count"
      >合 计:<strong> {{ this.list.length }} </strong></span
    >
    <!-- 清空 -->
    <button class="clear-completed" @click="del">清空任务</button>
  </footer>
</template>

<script>
export default {
  name: "ToDoFooter",
  props: {
    list: Array,
  },
  methods: {
    //清空列表
    del() {
      this.$emit("delInfo");
    },
  },
};
</script>

<style></style>
