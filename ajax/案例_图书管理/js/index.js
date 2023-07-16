/**
 * 目标1：渲染图书列表
 *  1.1 获取数据
 *  1.2 渲染数据
 */
let creator = "小尬";
//封装渲染图书列表的函数
function bookRender() {
    axios({
        method: 'get',
        url: "http://hmajax.itheima.net/api/books",
        params: {
            creator,
        }
    }).then(result => {
        let htmlstr = result.data.data.map((el, index) => {
            let { bookname, author, publisher } = el;
            return ` <tr>
          <td>${index + 1}</td>
          <td>${bookname}</td>
          <td>${author}</td>
          <td>${publisher}</td>
          <td data-id="${el.id}">
            <span class="del  ">删除</span>
            <span class="edit">编辑</span>
          </td>
        </tr> `;
        }).join("");
        let bookList = document.querySelector('.list');
        bookList.innerHTML = htmlstr;
        console.log(result.data.data);
    })
        .catch(err => console.log(err))
}
bookRender();
//获取添加图书的元素
let modalDom = document.querySelector('.add-modal');
//变成bootstrap对象
let modaladd = new bootstrap.Modal(modalDom);

/* data: {
    Object
    author :""
    bookname:""
    publisher:""
} */

//获取确认添加按钮
let addBtn = document.querySelector('.add-btn');
//添加图书
addBtn.onclick = function () {
    //获取新增form表单的元素
    let addForm = document.querySelector('.add-form');
    //使用form-serialize来获取表单的所有值
    const data = serialize(addForm, { hash: true, empty: true });
    //对data进行解构
    let { author, bookname, publisher } = data;//可以不对data进行解构，直接使用展开运算符
    //向服务端发送新增图书信息
    axios({
        url: 'http://hmajax.itheima.net/api/books',
        method: 'post',
        data: {
            bookname,
            author,
            publisher,
            creator
        }
    }).then(result => {
        if (result.data.message === "添加图书成功") {
            let ts = document.querySelector('.custom-alert');
            ts.style.opacity = '1';
            setTimeout(() => ts.style.opacity = '0', 2000)
            bookRender();
            //重置表单
            addForm.reset();
            //关闭
            modaladd.hide();
        }

    })


}
//删除图书
document.addEventListener('click', e => {
    //使用事件委托
    if (e.target.classList.contains('del')) {
        //获取图位id
        let id = e.target.parentNode.dataset.id;
        console.log(id);
        //后台删除图位
        axios({
            url: `http://hmajax.itheima.net/api/books/${id}`,
            method: 'delete',

        }).then(result => {
            console.log(result);
            if (result.data.message === "删除图书成功") {
                bookRender();
            }
        }).catch(err => console.log(err))

    }
})
//四.编辑图书
//1.弹窗的显示与隐藏
let editModal = document.querySelector('.edit-modal');
let editModaladd = new bootstrap.Modal(editModal);
document.addEventListener('click', e => {
    if (e.target.classList.contains('edit')) {
        //通过id获取回显数据
        let backId = e.target.parentNode.dataset.id;
        console.log(backId);
        //通过id获取数据
        axios({
            url: `http://hmajax.itheima.net/api/books/${backId}`,
        }).then(result => {
            let bookObj = result.data.data;
            //通过遍历对象数组快速赋值
            const keys = Object.keys(bookObj);
            console.log(keys);// ['id', 'bookname', 'author', 'publisher']
            //遍历赋值
            keys.forEach(key => {
                document.querySelector(`.edit-form .${key}`).value = bookObj[key];

            })
            /*   let { bookname, author, publisher } = bookObj;
              document.querySelector('.edit-form .bookname').value = bookname;
              document.querySelector('.edit-form .author').value = author;
              document.querySelector('.edit-form .publisher').value = publisher; */
        }
        )
        editModaladd.show();
    }
    //获取关闭按钮

})
let editClose = document.querySelector('.edit-btn');
editClose.onclick = function () {
    //提交保存修改并刷新列表
    let editForm = document.querySelector('.edit-form');
    //对对象进行解构，以便快速拿到值
    const { id, bookname, author, publisher } = serialize(editForm, { hash: true, empty: true });
    //向服务器发送修改请求
    axios({
        url: `http://hmajax.itheima.net/api/books/${id}`,
        method: 'put',
        data: {
            bookname, author, publisher, creator
        }
    }).then(result => {
        bookRender();
        //关闭编辑图书弹框
        editModaladd.hide();

    }).catch(err => console.log(err));


}