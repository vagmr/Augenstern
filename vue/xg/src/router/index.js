//引入插件
import VueRouter from "vue-router";
//引入阉割版vue
import Vue from "vue";
//导入路由组件
//@代表src目录
import FindMusic from '@/views/Find.vue';
import MyFridend from '@/views/Friend.vue';
import MyMusic from '@/views/My.vue';
import OtherPage from '@/views/OtherPage.vue';
//导入主页组件
import HomePage from '@/views/Home.vue';
//导入搜索页
import SearchPage from '@/components/Search.vue';
import NotFound from '@/components/NotFound.vue';
import Layout from '@/views/Layout.vue';
import ArticleDetail from '@/views/ArticleDetail.vue';
import ArticlePage from '@/views/Article.vue';
import Collect from '@/views/Collect.vue';
import User from '@/views/User';
import Like from '@/views/Like';

//安装插件
Vue.use(VueRouter);
//创建路由对象
export const router = new VueRouter({
    mode: 'history',
    //配置路由规则
    routes: [
        //首页重定向
        { path: '/', redirect: '/home' },
        { path: '/find', component: FindMusic },
        { path: '/friend', component: MyFridend },
        { path: '/music', component: MyMusic },
        { path: '/other', component: OtherPage },
        { path: '/home', component: HomePage },
        { path: '/search', component: SearchPage },
        {
            path: '/mjindex', component: Layout,
            //配置子路由
            children: [{
                path: '/artic', component: ArticlePage
            },
            { path: '/collect', component: Collect },
            { path: '/user', component: User },
            { path: '/like', component: Like },
            ]
        },
        { path: '/dtl', component: ArticleDetail },

        //404页面
        { path: '*', component: NotFound },
    ],

});