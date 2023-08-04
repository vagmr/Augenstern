<template>
  <div class="table-case">
    <MyTab :list="goods">
      <template #thead>
        <tr>
          <th>编号</th>
          <th>图片</th>
          <th>名称</th>
          <th width="100px">标签</th>
        </tr>
      </template>
      <!-- td部分 -->
      <!-- 使用作用域插槽解构子组件传来的数组 -->
      <template #td="{ el, index }">
        <td>{{ index + 1 }}</td>
        <td>
          <img :src="el.picture" />
        </td>
        <td>{{ el.name }}</td>
        <td><MyTag v-model="el.tag" /></td>
      </template>
    </MyTab>
  </div>
</template>

<script>
import MyTab from "./MyTab.vue";
import MyTag from "./MyTag.vue";
export default {
  name: "ShopList",
  components: { MyTab, MyTag },
  data() {
    return {
      goods: [
        {
          id: 101,
          picture:
            "https://yanxuan-item.nosdn.127.net/f8c37ffa41ab1eb84bff499e1f6acfc7.jpg",
          name: "梨皮朱泥三绝清代小品壶经典款紫砂壶",
          tag: "茶具",
        },
        {
          id: 102,
          picture:
            "https://yanxuan-item.nosdn.127.net/221317c85274a188174352474b859d7b.jpg",
          name: "全防水HABU旋钮牛皮户外徒步鞋山宁泰抗菌",
          tag: "男鞋",
        },
        {
          id: 103,
          picture:
            "https://yanxuan-item.nosdn.127.net/cd4b840751ef4f7505c85004f0bebcb5.png",
          name: "毛茸茸小熊出没，儿童羊羔绒背心73-90cm",
          tag: "儿童服饰",
        },
        {
          id: 104,
          picture:
            "https://yanxuan-item.nosdn.127.net/56eb25a38d7a630e76a608a9360eec6b.jpg",
          name: "基础百搭，儿童套头针织毛衣1-9岁",
          tag: "儿童服饰",
        },
      ],
      tag: [],
    };
  },
};
</script >

