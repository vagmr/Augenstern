<template>
  <div class="usersInfo">
    <h3>我是个人信息组件</h3>
    <div v-color="color[0]">姓名：{{ name }}</div>
    <div>年龄：{{ age }}</div>
    <div>是否单身:{{ isSingle ? "是" : "否" }}</div>
    <div>座驾:{{ car }}</div>
    <div>
      兴趣爱好:
      <li v-for="(h, index) in hobby" :key="index">
        {{ h }}
      </li>
    </div>
    <input type="text" :value="msg" @input="msg = $event.target.value" />
    <div class="app">
      <div v-if="isShowEdit">
        <input type="text" v-model="editValue" ref="inp" />
        <button>确认</button>
      </div>
      <div v-else>
        <span>{{ title }}</span>
        <button @click="editFn">编辑</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "UsersInfo",
  data() {
    return {
      msg: "v-model的原理",
      title: "大标题",
      isShowEdit: false,
      editValue: "",
      color: ["green", "skyblue"],
    };
  },
  methods: {
    editFn() {
      this.isShowEdit = true;
      this.$nextTick(() => {
        this.$refs.inp.focus();
      });
      //使用updated也可行
    },
  },

  props: {
    name: {
      type: String,
      request: true,
    },
    age: {
      type: Number,
      default: 18,
    },
    isSingle: {
      type: Boolean,
      default: true,
    },
    car: {
      type: String,
      default: "无",
    },
    hobby: {
      type: Array,
      default: () => ["吃饭", "睡觉", "打豆豆"],
    },
  },
};
</script>

<style scoped>
.usersInfo {
  width: 400px;
  border: 3px solid #ff6545;
  padding: 10px;
}
.usersInfo > div {
  font-family: "楷书";
  font-size: 17px;
  height: 30px;
  line-height: 30px;
  color: orchid;
}
.usersInfo div li {
  list-style: none;
  display: inline;
}
</style>