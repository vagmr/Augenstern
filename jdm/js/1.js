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
})