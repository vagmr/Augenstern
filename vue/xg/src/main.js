//引入阉割版vue
import Vue from "vue";
//引入app组件
import App from "./App.vue";
//引入插件
import { obj } from "./plugins";
Vue.use(obj);
//引入路由
import { router } from './router/index';
//关闭生产提示
Vue.config.productionTip = false;
new Vue({
    //渲染页面
    render: h => h(App),
    //挂载路由(完整写法 router:router)
    router,
    //绑定根元素
}).$mount('#App');