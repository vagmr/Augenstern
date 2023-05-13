var myName = 'vagmr';
var version = 0.01;
var about = 'dev';
alert(version + ' ' + myName + ' ' + about);
alert(`${version}\t${myName}\t${about} `);
// alert(myName);
// alert(about);
function test() {
    alert("播放")
    var num = prompt('请输入一个数字');
    /* if (num < 10) {
        var numstr = num.toString();
        numstr = '0' + numstr;
        alert(numstr);
    } */
    num < 10 ? alert('0' + num) : alert(num);
    var year = prompt('请输入你的出生年份');
    if (year % 4 == 0 && year % 100 != 0 || year % 400 == 0) {
        alert('年份是闰年');
    }
    else {
        alert('不是闰年');
    }
    var age = 2023 - year;
    if (age <= 0 | age > 120) {
        alert('不要恶搞');
    }
    if (age > 0 & age <= 120) {
        alert('年龄为' + age);
    }
}