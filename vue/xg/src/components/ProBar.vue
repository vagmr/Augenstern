<template>
  <div class="ProBar">
    <div :class="inner" :style="{ width: wS + '%' }"></div>
    <span>{{ wS }} %</span>
    <!-- // eslint-disable-next-line vue/no-mutating-props -->
    <button @click="wS++">点我增加进度条</button>
    <button @click.once="anima">点我使进度条自己移动</button>
  </div>
</template>

<script>
export default {
  name: "ProBar",
  data() {
    return {
      wS: this.w,
      inner: ["inner"],
      protime: null,
    };
  },
  props: {
    w: {
      type: Number,
      default: 0,
      validator(val) {
        if (val >= 0 && val <= 100) return true;
        else {
          console.error("传值必须在0-100之间");
          return false;
        }
      },
    },
  },
  methods: {
    anima() {
      this.inner.push("ani");
      this.wS = 0;
      if (this.protime) {
        clearInterval(this.protime);
      }
      this.protime = setInterval(() => {
        if (this.wS < 100) {
          this.wS++;
        } else {
          this.wS = 0;
        }
      }, 30);
    },
  },
};
</script>

<style>
/* //进度条样式设置 */
.ProBar {
  position: absolute;
  bottom: 10px;
  left: 50%;
  transform: translateX(-50%);
  width: 600px;
  height: 30px;
  border: 3px solid #ccc;
  background-color: black;
  box-sizing: border-box;
  border-radius: 15px;
  text-align: center;
}
.inner {
  height: 100%;
  background: linear-gradient(to right, orange, rgb(188, 13, 100));
  border-radius: 15px;
}
.ProBar span {
  font-family: "行书";
  font-size: 18px;
  color: rgb(170, 25, 95);
}
.ProBar button {
  display: block;
  width: 200px;
  height: 50px;
  text-align: center;
  line-height: 50px;
  background-color: aquamarine;
  font-weight: 700;
  color: #9e1010;
  margin: 12px 0 0 200px;
}
@keyframes pro {
  from {
    width: 0;
  }
  to {
    width: 100%;
  }
}
.ani {
  animation: pro 3s linear infinite;
}
</style>