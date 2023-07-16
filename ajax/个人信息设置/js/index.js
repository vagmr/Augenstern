/**
 * 目标1：信息渲染
 *  1.1 获取用户的数据
 *  1.2 回显数据到标签上
 * */

// 获取用户的数据
const creator = 'xg';
axios({
    url: 'http://hmajax.itheima.net/api/settings',
    method: 'get',
    params: { creator },
}).then(result => {
    //avatar: 'http://hmajax.itheima.net/avatar/avatar2.png', nickname: 'itheima', email: 'itheima@itcast.cn', desc: '我是xg', gender: 0}
    let dataObj = result.data.data;
    let dataK = Object.keys(result.data.data);
    dataK.forEach(el => {
        if (el === 'avatar') {
            document.querySelector('.prew').src = dataObj[el];
        }
        //单独处理性别
        else if (el === 'gender') {
            let genderList = document.querySelectorAll('.gender');
            let gNum = dataObj[el];
            //返回的序号作为索引确定男女
            genderList[gNum].checked = true;
        }
        else {
            //其他常规处理，赋予默认内容,以获取到的键值作为类名
            document.querySelector(`.${el}`).value = dataObj[el];
        }
    })
}).catch(error => console.log(error))
//图像上传加回显
//给文件上传的表单绑定change事件
document.querySelector('.upload').addEventListener('change', e => {
    //新建formdata对象
    let fd = new FormData();
    fd.append('avatar', e.target.files[0]);
    fd.append('creator', creator);
    axios({
        url: 'http://hmajax.itheima.net/api/avatar',
        method: 'PUT',
        data: fd,
    }).then(result => {
        let imgUrl = result.data.data.avatar;
        document.querySelector('.prew').src = imgUrl;
    })
})
const userForm = document.querySelector('.user-form');
userForm.addEventListener('submit', () => {
    //修改个人信息

    const formData = serialize(userForm, { hash: true, empty: true });
    formData.creator = creator;

    formData.gender = +formData.gender;
    console.log(formData);
    //提交数据到服务器
    axios({
        url: 'http://hmajax.itheima.net/api/settings',
        method: 'put',
        data: formData,
    }).then(result => {
        let toastDom = document.querySelector('.myToast');
        let toast = new bootstrap.Toast(toastDom);
        toast.show();
    }).catch(error => console.log(error))
})