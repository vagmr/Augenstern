<template>
  <div>
    <BA />
    <BB />
  </div>
</template>

<script>
import BA from "./BaseA";
import BB from "./BaseB";

export default {
  name: "BaseIndex",
  components: { BA, BB },
};
</script>

<style>
</style>