var btn = document.querySelector('.b');
var dd = document.querySelector('.dd');
var flag = 0;
btn.onclick = function () {
    if (flag == 0) {
        console.log('执行');
        dd.style.display = 'none';
        flag = 1;
    }
    if (flag == 1) {
        dd.style.display = 'block';
        flag = 0;
    }
}