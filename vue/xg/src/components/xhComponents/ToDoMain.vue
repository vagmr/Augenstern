<template>
  <!-- 列表区域 -->
  <section class="main">
    <ul class="todo-list">
      <li class="todo" v-for="el in list" :key="el.id">
        <div class="view">
          <span class="index">{{ el.id }}.</span>
          <label>{{ el.name }}</label
          ><i id="time">{{ el.time }}</i>
          <input type="checkbox" v-model="el.done" class="check" /><strong>{{
            el.done ? "完成" : "未完成"
          }}</strong>
          <button class="destroy" @click="delOne(el.id)"></button>
        </div>
      </li>
    </ul>
  </section>
</template>

<script>
export default {
  name: "ToDoMain",
  props: {
    list: Array,
  },
  data() {
    return {
      Hlist: this.list,
    };
  },
  methods: {
    delOne(id) {
      this.$emit("delOne", id);
    },
  },
};
</script>


<style></style>