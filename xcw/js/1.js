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
        oli.setAttribute("data-index", i);
        ol.appendChild(oli);
    }
    var index = 0;
    var timer = setInterval(function () {
        index++;
        var translateX = - w * index;
        ul.style.transition = "all 0.5s";
        ul.style.transform = 'translateX(' + translateX + "px" + ')';
        if (index == 3) {
            index = -2;
        }
    }, 2000)
    ol.children[0].className = "current";
}