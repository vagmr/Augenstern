window.onload = function () {
    function animate(obj, target, callback) {
        clearInterval(obj.timer);
        obj.timer = setInterval(function () {
            obj.speed = (target - obj.offsetLeft) / 10;
            obj.speed = obj.speed > 0 ? Math.ceil(obj.speed) : Math.floor(obj.speed);
            if (obj.offsetLeft == target) {
                clearInterval(obj.timer)
                //添加回调函数
                callback && callback();
            }
            else {
                obj.style.left = obj.offsetLeft + obj.speed + 'px';
            }
        }, 30);
    }
    var focus = document.querySelector('.focus');
    var ul = document.querySelector(".ful");
    var li = document.querySelectorAll('li');
    var w = focus.offsetWidth;
    console.log(li);
    var ol = document.querySelector('ol');
    for (var i = 0; i < li.length; i++) {
        var oli = document.createElement('li');
        ol.appendChild(oli);
    }
    var first = ul.children[0].cloneNode(true);
    ul.appendChild(first);
    var Two = ul.children[2].cloneNode(true);
    ul.insertBefore(Two, ul.firstChild);
    var index = 0;
    var timer = setInterval(function () {
        index++;
        var translateX = - w * index;
        ul.style.transition = "all 0.5s";
        ul.style.transform = 'translateX(' + translateX + "px" + ')';
    }, 2000)
    ol.children[0].className = 'current';
    ul.addEventListener('transitionend', function () {
        if (index >= 3) {
            index = 0;
            ul.style.transition = "none";
            var translateX = - w * index;
            ul.style.transform = 'translateX(' + translateX + "px" + ')';
        } else if (index < 0) {
            index = 2;
            ul.style.transition = "none";
            var translateX = - w * index;
            ul.style.transform = 'translateX(' + translateX + "px" + ')';

        }
        ol.querySelector('.current').classList.remove('current');
        ol.children[index].classList.add('current');
    })
    //手指滑动轮播图
    let start = 0;
    ul.addEventListener('touchstart', function (e) {
        start = e.targetTouches[0].pageX;

    })
    ul.addEventListener('touchmove', function (e) {
        let moveX = e.targetTouches[0].pageX - start;
        let translateX = - w * index + moveX;
        ul.style.transform = 'translateX(' + translateX + 'px)';
    })

}