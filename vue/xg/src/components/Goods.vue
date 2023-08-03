<template>
  <div class="box">
    <h1>{{ title }}</h1>
    <h2>{{ time }}</h2>
    <h3 @click="showInfo">{{ phoneName }} --- {{ price }}</h3>
  </div>
</template>

<script>
import { showInfo } from "../common";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Goods",
  data() {
    return {
      title: "这是一个组件",
      time: new Date().toLocaleString(),
    };
  },
  props: {
    phoneName: {
      type: String,
      default: "华为",
    },
    price: {
      type: Number,
      default: 6999,
    },
  },
  mixins: [showInfo],
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #25252b;
}

.box {
  position: relative;
  width: 400px;
  height: 400px;
  background: repeating-conic-gradient(
    from var(--a),
    #ff2770 0%,
    #ff2770 5%,
    transparent 5%,
    transparent 40%,
    #ff2770 50%
  );
  animation: rander 4s linear infinite;
  border-radius: 20px;
  color: white;
}

@property --a {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

@keyframes rander {
  0% {
    --a: 0deg;
  }

  100% {
    --a: 360deg;
  }
}

.box::before {
  content: "";
  position: absolute;
  width: 100%;
  height: 100%;
  background: repeating-conic-gradient(
    from var(--a),
    #45f3ff 0%,
    #45f3ff 5%,
    transparent 5%,
    transparent 40%,
    #45f3ff 50%
  );
  animation: rander 4s linear infinite;
  animation-delay: -1s;
  border-radius: 20px;
}

.box::after {
  content: "";
  position: absolute;
  inset: 8px;
  background: #2d2d39;
  border-radius: 15px;
  border: 8px solid #25252b;
}
h1 {
  position: absolute;
  z-index: 999;
  top: 50%;
  left: 50%;
  transform: translateX(-50%) translateY(-50%);
}
h2 {
  position: absolute;
  z-index: 999;
  top: 55%;
  left: 24%;
}
h3 {
  position: absolute;
  z-index: 999;
  top: 30px;
  left: 10px;
  color: #b40e45;
  font-size: 20px;
}
</style>