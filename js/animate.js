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