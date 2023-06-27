window.onload = function () {
    function animate(obj, target, callback) {
        clearInterval(obj.timer);
        obj.timer = setInterval(function () {
            obj.speed = (target - obj.offsetLeft) / 10;
            obj.speed = obj.speed > 0 ? Math.ceil(obj.speed) : Math.floor(obj.speed);
            if (obj.offsetLeft == target) {
                clearInterval(obj.timer)
                //添加回调函数
                if (callback) { callback(); }
            }
            else {
                obj.style.left = obj.offsetLeft + obj.speed + 'px';
            }
        }, 30);
    }
    var divml = document.querySelector('.ml');
    var arrow1 = document.querySelector('.arrow-l');
    var arrow2 = document.querySelector('.arrow');
    var num = 0;
    //用来控制小圆圈随轮播图一起变化
    var cricle = 0;

    //切换按钮的显示与隐藏
    divml.addEventListener('mouseover', function () {
        arrow1.style.display = 'block';
        arrow2.style.display = 'block';
    });
    divml.addEventListener('mouseleave', function () {
        arrow1.style.display = 'none';
        arrow2.style.display = 'none';
    });
    //end=======================================
    //动态创建小圆圈
    var ul = divml.querySelector('ul');
    var li = ul.querySelectorAll('li');
    var ol = document.querySelector('.circle');
    for (var i = 0; i < li.length; i++) {
        var oli = document.createElement('li');
        //通过自定义属性记录当前小圆圈的索引号
        oli.setAttribute('data-index', i);
        ol.appendChild(oli);
    }
    // 设置第一个小按钮为红色
    ol.children[0].className = 'current';
    // 循环小圆圈点击注册事件
    var mlWidth = divml.offsetWidth;
    for (var i = 0; i < ol.children.length; i++) {
        ol.children[i].onclick = function () {
            for (var i = 0; i < ol.children.length; i++) {
                ol.children[i].className = ' ';
            }
            this.className = 'current';
            //获取img所在盒子的宽度   
            var index = this.getAttribute('data-index');
            //点击小圆圈后把索引给num，以使小圆圈和按钮同步
            num = index;
            //点击小圆圈后把索引给cricle，以使小圆圈和按钮同步
            cricle = index;
            console.log(mlWidth);
            console.log(index);
            animate(ul, -index * mlWidth);
        }
    }
    //克隆第一张图片放到最后
    var first = ul.children[0].cloneNode(true);
    ul.appendChild(first);
    //end=====================================
    // 通过按钮切换轮播图

    arrow2.addEventListener('click', function () {
        if (num == 4) {
            ul.style.left = '0';
            num = 0;
        }
        num++;
        animate(ul, - num * mlWidth);
        cricle++;
        if (cricle == ol.children.length) {
            cricle = 0;
        }
        change();
    })
    arrow1.addEventListener('click', function () {
        if (num == 0) {
            num = ul.children.length - 1;
            ul.style.left = - num * mlWidth + 'px';
        }
        num--;
        animate(ul, - num * mlWidth);
        cricle--;
        if (cricle < 0) {
            cricle = 3;
        }
        change();
    })
    function change() {
        for (var i = 0; i < ol.children.length; i++) {
            ol.children[i].className = ' ';
        }
        ol.children[cricle].className = 'current';
    }
}