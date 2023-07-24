/**
     * 目标：把所有商品分类“同时”渲染到页面上
     *  1. 获取所有一级分类数据
     *  2. 遍历id，创建获取二级分类请求
     *  3. 合并所有二级分类Promise对象
     *  4. 等待同时成功后，渲染页面
    */
//获取所有一级分类数据
axios({ url: 'http://hmajax.itheima.net/api/category/top' }).then(res => {
    const promiseList = res.data.data.map(el => {
        return axios({ url: 'http://hmajax.itheima.net/api/category/sub', params: { id: el.id } })
    })
    const p = Promise.all(promiseList)
    p.then(res => {
        // 4. 等待同时成功后，渲染页面
        let htmlStr = res.map(el => {
            return `<div class="item">
                <h3>${el.data.data.name}</h3>
                <ul>
                    ${el.data.data.children.map(el => {
                return ` <li>
                        <a href="javascript:;">
                            <img src="${el.picture}">
                            <p>${el.name}</p>
                        </a>
                    </li>`
            }).join('')}
               </ul>
            </div>`;
        }).join('');
        console.log(htmlStr);
        document.querySelector('.sub-list').innerHTML = htmlStr;
    })
})