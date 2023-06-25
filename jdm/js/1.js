window.addEventListener("DOMContentLoaded", function () {
    // 顶部区域
    var close = document.querySelector('#v1');
    var app_bar = document.querySelector('.app');
    close.addEventListener('click', function () {
        app_bar.style.display = 'none';
    })
    //链接跳转
    var a = document.querySelector('#v2');
    a.addEventListener('click', function () {
        location.assign('https://about.vagmrgpt.top');
    })
    // 顶部区域end
    // 倒计时
    var hour = document.querySelector('.h');
    var minute = document.querySelector('.m');
    var second = document.querySelector('.s');
    var inputTime = +new Date('2023-6-30 18:00:00');
    function Countdown() {
        var nowTime = +new Date();//返回当前时间的毫秒数
        var countTime = (inputTime - nowTime) / 1000;//返回剩余时间的秒数
        var h = parseInt(countTime / 60 / 60 % 24);//通过取模找出不足一天的
        h = h < 10 ? '0' + h : h;
        hour.innerHTML = h;
        var m = parseInt(countTime / 60 % 60);//分
        m = m < 10 ? '0' + m : m;
        minute.innerHTML = m;
        var s = parseInt(countTime % 60);
        s = s < 10 ? '0' + s : s;
        second.innerHTML = s;
    }
    setInterval(Countdown, 1000);
})