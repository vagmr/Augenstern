/**
 * 目标：封装_简易axios函数_获取省份列表
 *  1. 定义myAxios函数，接收配置对象，返回Promise对象
 *  2. 发起XHR请求，默认请求方法为GET
 *  3. 调用成功/失败的处理程序
 *  4. 使用myAxios函数，获取省份列表展示
*/
function myAxios(config) {
    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        //为myAxios增加查询参数
        if (config.params) {
            const paramsObj = new URLSearchParams(config.params);
            const queryStr = paramsObj.toString();
            config.url += `?${queryStr}`;
        }

        xhr.open(config.method || 'get', config.url);
        xhr.addEventListener('loadend', () => {
            if (xhr.status >= 200 && xhr.status < 300) {
                resolve(JSON.parse(xhr.response))
            }
            else {
                reject(new Error(xhr.response))
            }
        })
        //判断是否有data数据发送请求体
        if (config.data) {
            let data = JSON.stringify(config.data);
            xhr.setRequestHeader('content-type', 'application/json');
            xhr.send(data);
        }
        else {
            xhr.send()
        }

    })
}
myAxios({
    url: 'http://hmajax.itheima.net/api/province',
}).then(res => {
    console.log(res);
    document.querySelector('.prv-p').innerHTML = res.list.join('<br>');
}).catch(error => {
    console.log(error);
})
window.onload = function () {
    document.querySelector('.zc').addEventListener('click', () => {
        console.log('进来了');
        let username = 'xXXXXXXX';
        let password = 'XXXXXXXX';
        myAxios({
            url: "http://hmajax.itheima.net/api/register",
            method: "post",
            data: {
                username,
                password
            }
        }).then(res => {
            console.log(res);
        }).catch(error => {
            console.log(error);
        })
    })
}