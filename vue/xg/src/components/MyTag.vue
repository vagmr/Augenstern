<template>
  <div class="my-tag">
    <!-- 可以使用v-focus(自定义指令)实现 -->
    <input
      v-if="isEdit"
      class="input"
      type="text"
      placeholder="输入标签"
      ref="ipt"
      @blur="isEdit = false"
      :value="value"
      @keyup.enter="fixValue"
    />
    <div class="text" v-else @dblclick="Hclick">{{ value }}</div>
  </div>
</template>

<script>
export default {
  name: "MyTag",
  data() {
    return {
      isEdit: false,
    };
  },
  props: {
    value: {
      type: String,
    },
  },
  methods: {
    //使用async await实现
    async Hclick() {
      this.isEdit = true;
      await this.$nextTick();
      this.$refs.ipt.focus();
    },
    fixValue(e) {
      if (e.target.value.trim() === "") {
        alert("输入不能为空");
        return;
      }
      this.$emit("input", e.target.value);
      this.isEdit = false;
    },
  },
};
</script>

<style lang="less" scoped>
.my-tag {
  cursor: pointer;
  .input {
    appearance: none;
    outline: none;
    border: 1px solid #ccc;
    width: 100px;
    height: 40px;
    box-sizing: border-box;
    padding: 10px;
    color: #666;
    &::placeholder {
      color: #666;
    }
  }
}
</style>