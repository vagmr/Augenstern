//引入阉割版vue
import Vue from "vue";
//引入app组件
import App from "./App.vue";
//引入插件
import { obj } from "./plugins";
import VueRouter from "vue-router";
//导入路由组件
import FindMusic from './views/Find.vue';
import MyFridend from './views/Friend.vue';
import MyMusic from './views/My.vue';
//安装插件
Vue.use(VueRouter);
Vue.use(obj);
//创建路由对象
const router = new VueRouter({
    //配置路由规则
    routes: [
        { path: '/find', component: FindMusic },
        { path: '/friend', component: MyFridend },
        { path: '/music', component: MyMusic }
    ]
});
//关闭生产提示
Vue.config.productionTip = false;
new Vue({
    //渲染页面
    render: h => h(App),
    //挂载路由(完整写法 router:router)
    router,
    //绑定根元素
}).$mount('#App');