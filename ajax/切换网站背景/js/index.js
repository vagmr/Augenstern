/**
 * 目标：网站-更换背景
 *  1. 选择图片上传，设置body背景
 *  2. 上传成功时，"保存"图片url网址
 *  3. 网页运行后，"获取"url网址使用
 * */
//获取file表单
document.querySelector('.bg-ipt').addEventListener('change', e => {
    //新建formdata对象
    const fd = new FormData();
    //键值对形式
    fd.append('img', e.target.files[0]);
    //向服务端发送请求
    axios({
        method: 'post',
        url: 'http://hmajax.itheima.net/api/uploadimg',
        data: fd
    }).then(result => {
        //获取到图片路径
        let imgUrl = result.data.data.url;
        //为body设置背景图片
        document.body.style.backgroundImage = `url(${imgUrl})`;
    })
})