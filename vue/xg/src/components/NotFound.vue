<template>
  <div class="NotFound">
    <h1>404</h1>
    <h1>This Page is Not Found</h1>
  </div>
</template>

<script>
export default {
  name: "NotFound",
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
.NotFound {
  position: relative;
  left: 50%;
  margin-top: 10%;
  transform: translateX(-50%);
  text-align: center;
  height: 200px;
  width: 400px;
  background-color: orange;
  line-height: 100px;
}
</style>