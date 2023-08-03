import Vue from "vue";
import App from "./App.vue";
//引入插件
import { obj } from "./plugins";
//安装插件
Vue.use(obj);
//关闭生产提示
Vue.config.productionTip = false;
new Vue({
    render: h => h(App)
}).$mount('#App');