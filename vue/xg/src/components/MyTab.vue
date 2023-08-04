<template>
  <table class="my-table">
    <thead>
      <!-- //使用具名插槽使结构更灵活 -->
      <slot name="thead"></slot>
    </thead>
    <tbody>
      <tr v-for="(el, index) in list" :key="el.id">
        <slot name="td" :el="el" :index="index"> </slot>
      </tr>
    </tbody>
  </table>
</template>

<script>
// import MyTag from "./MyTag";

export default {
  name: "MyTab",
  //   components: { MyTag },
  props: {
    list: Array,
  },
};
</script>

<style lang="less" scoped>
.table-case {
  width: 1000px;
  margin: 50px auto;
  img {
    width: 100px;
    height: 100px;
    object-fit: contain;
    vertical-align: middle;
  }
}

.my-table {
  width: 100%;
  border-spacing: 0;
  img {
    width: 100px;
    height: 100px;
    object-fit: contain;
    vertical-align: middle;
  }
  th {
    background: #f5f5f5;
    border-bottom: 2px solid #069;
  }
  td {
    border-bottom: 1px dashed #ccc;
  }
  td,
  th {
    text-align: center;
    padding: 10px;
    transition: all 0.5s;
    &.red {
      color: red;
    }
  }
  .none {
    height: 100px;
    line-height: 100px;
    color: #999;
  }
}
</style>