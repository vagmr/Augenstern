function vagmr() {
    inputName = prompt('请输入你的名字');
    inputage = prompt('请输入你的年龄');
    inputver = prompt('请输入你的版本');
    alert('名字是' + `${inputName}\n` + '年龄是' + `${inputage}\n`
        + '版本是' + `${inputver}`)
}
// function stars() {
//     var cols = prompt('请输入行数');
//     var rows = prompt('请输入列数');
//     for (var i = 1; i <= cols; i++) {
//         var str = '';
//         for (var j = 0; j <= rows - i; j++) {
//             str += '☆'; // 将星号添加到字符串末尾
//         }
//         console.log(str); // 在内部循环结束后输出字符串
//     }

//     alert('打印结束')
// }
function stars() {
    var cols = prompt('请输入行数');
    var str = '';
    for (var i = 1; i <= cols; i++) {
        for (var j = 1; j <= i; j++) {
            // str += '☆';
            // 将星号添加到字符串末尾
            str += j + 'x' + i;
            str += '\t';
        }
        str += '\n';
        // 在内部循环结束后输出字符串
    }
    console.log(str);
    alert('打印结束')
    var ary = [65, 67, 123, 98, 12, 34, 13, 100, 90];
    for (var i = 0; i < ary.length; i++) {
        for (var j = 0; j < ary.length - i; j++) {
            if (ary[j] > ary[j + 1]) {
                var temp;
                temp = ary[j + 1];
                ary[j + 1] = ary[j];
                ary[j] = temp;
            }

        }
    }
    console.log(ary);
}
// ======================================================
/* function test() {
    var start = 0;
    var end = arguments.length - 1;
    while (start < end) {
        var temp;
        temp = arguments[end]
        arguments[end] = arguments[start];
        arguments[start] = temp;
        //更新值以交换下一对元素
        start++;
        end--;
    }
    return arguments;
}
console.log(test(prompt('依次输入数组的值'), prompt('2'), prompt(), prompt(), prompt())); */
// ==================================================================
function reverse(ary) {
    var newAry = [];
    for (var i = ary.length - 1; i >= 0; i--) {
        newAry[newAry.length] = ary[i];
    }
    return newAry;
}
console.log(reverse([98, 9, 12, 33, 45, 66, 87, 90, 12, 311]));
/* if (1 < 2) {
    var test = 10;
}没有块级作用域，结构体内变量可以直接在外面调用
console.log(test); */
/* 函数创建方法
1.通过json，字面值，var创建 */
var obj = {
    uName: 16,
    age: 18,
    addres: 'lundon',
    show: function () {
        alert('json');
    }
}
// 2.通过new Object() 创建对象
var obj2 = new Object();
obj2.name = '丁真';
obj2.show = function () {
    console.log('对象');
}
// 3.通过构造函数创建对象
class Start {
    constructor(name, type, hp, attack) {
        this.name = name;
        this.type = type;
        this.hp = hp;
        this.attack = attack;
        this.gj = function () {
            console.log('造成了' + this.attack + '点伤害');
        };
    }
}
var lp = new Start('廉颇', '战士', 3000, 100);
lp.gj();
// 建议计算机制作
function info() {
    var tan = prompt('下面是一个简易的计算器\n1.运算\n2.减法运算\n3.乘法运算\n4.除法运算\n5.退出');
    //函数的特点，因为本身的特性，函数调用执行完毕，就垃圾回收
    function jisuan(shuzi) {
        var num1 = parseInt(prompt('第一个数字'));
        var num2 = parseInt(prompt('第二个数字'));
        var result;
        switch (parseInt(shuzi)) {
            // 判断要输入的状态
            case 1:
                result = num1 + num2;
                break;
            case 2:
                result = num1 - num2;
                break;
            case 3:
                result = num1 * num2;
                break;
            case 4:
                result = num1 / num2;
                break;
            case 5:
                break;
        }
        alert(result);
        tan = prompt('1.+运算\n2.减法运算\n3.乘法运算\n4.除法运算\n5.退出');

    }

    // 我们只能让他重复的输入，重复的调用函数
    // 2.接下来交给函数来完成，包装在一个函数中，需要的时候，我们就调用函数

    while (1 == 1) {
        if (tan == '1') {
            jisuan('1');
        }
        if (tan == '2') {
            jisuan('2');
        }
        if (tan == '3') {
            jisuan('3');
        }
        if (tan == '4') {
            jisuan('4');
        }
        if (tan == '5') {
            break;
        }
    }
}
/* alert('欢迎使用简易计算器' + '\n' +
'1,加法运算' + '\n' + '2,减法运算' +
'\n' + '3.乘法运算' + '\n' + '4,除法运算' + '\n'
+ '退出');
var opt = prompt('输入你的选项');
var num1 = prompt('请输入数字1');
var num2 = prompt('请输入数字2');
var obj = new Calmulicate();
while (opt != 5) {
switch (opt) {
case '1':
    var result = obj.add(num1, num2);
    alert('结果为' + result);
    break;
case '2':
    var result = obj.subtract(num1, num2);
    alert('结果为' + result);
    break;
case '3':
    var result = obj.multiply(num1, num2);
    alert('结果为' + result);
    break;
case '4':
    var result = obj.divide(num1, num2);
    alert('结果为' + result);
    break;
default:
    alert('输入有误，请重新输入');
    break;
}
opt = prompt('输入你的选项');
}
}

class Calmulicate {
constructor() {
this.add = function (num1, num2) {
return Number(num1) + Number(num2);
}
this.subtract = function (num1, num2) {
return Number(num1) - Number(num2);
}
this.multiply = function (num1, num2) {
return Number(num1) * Number(num2);
}
this.divide = function (num1, num2) {
return Number(num1) / Number(num2);
}
}
}
*/
// alert(new Date('YYYY-MM-DD hh:mm:ss'))
function getRandom(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min; //含最大值，含最小值
}
function guess() {
    var ranNum = getRandom(0, 50);
    var count = 0;
    while (count <= 4) {
        var num = prompt('猜0-50之间的一个数字')
        if (num == null) {
            alert('退出程序');
            break;
        }
        console.log(num);
        if (num > ranNum) {
            alert('你猜大了');
            count++;
        }
        else if (num < ranNum) {
            alert('你猜小了');
            count++;
        }
        else {
            alert('你猜对了');
            break;
        }
        if (count > 4) {
            alert('游戏结束');
        }
    }
};
// 使用 JavaScript 中的 Date 对象和计时器 setInterval()。每秒钟更新一次时间并显示在页面上
function updateTime() {
    const now = new Date();
    const year = now.getFullYear();
    const month = (now.getMonth() + 1).toString().padStart(2, '0');
    const day = now.getDate().toString().padStart(2, '0');
    const hour = now.getHours().toString().padStart(2, '0');
    const minute = now.getMinutes().toString().padStart(2, '0');
    const second = now.getSeconds().toString().padStart(2, '0');
    const timeStr = `${year}-${month}-${day} ${hour}:${minute}:${second}`;
    document.getElementById('time').textContent = timeStr;
};

setInterval(updateTime, 1000);
// 倒计时制作实现
/* 思路用用户输入的总毫秒数减去当前的总毫秒数，再换算成时分秒 */
/* function getCountDown(time){
    var currentTime = +new Date();
    var specifiedTime = +new Date(time);
    var remainingSeconds = Math.max(0, Math.floor((specifiedTime - currentTime) / 1000));
    var remainingMinutes = Math.floor(remainingSeconds / 60);
    var remainingHours = Math.floor(remainingSeconds / 3600);
    var remainingDays = Math.floor(remainingSeconds / 86400);
    var hours = Math.floor(remainingSeconds / 3600);
    var minutes = Math.floor((remainingSeconds % 3600) / 60);
    var seconds = remainingSeconds % 60;
    var remainingTime = `${remainingDays}天${hours}小时${minutes}分钟${seconds}秒`;
    return remainingTime
}  */
function getCountDown(time) {
    var currentTime = +new Date();
    var specifiedTime = +new Date(time);
    // 计算指定时间和当前时间之间剩余的总秒数，使用 Math.max(0, ...) 避免剩余秒数为负数。
    var remainingSeconds = Math.max(0, Math.floor((specifiedTime - currentTime) / 1000));
    // 计算出剩余的天数，即将剩余总秒数除以 86400（即每天的秒数），并向下取整。
    var remainingDays = Math.floor(remainingSeconds / 86400);
    remainingDays = remainingDays < 10 ? '0' + remainingDays : remainingDays;
    // 接着计算剩余的小时数。由于已经计算出剩余的天数，可以将剩余总秒数对 86400 取模，
    // 余数除以 3600（即每小时的秒数），向下取整即可。
    var remainingHours = Math.floor((remainingSeconds % 86400) / 3600);
    remainingHours = remainingHours < 10 ? '0' + remainingHours : remainingHours;
    // 接着计算剩余的小时数。由于已经计算出剩余的天数，可以将剩余总秒数对 3600(小时的秒数) 取模，得到不足1小时的
    // 余数除以 60（即每分钟的秒数），向下取整即可。
    var remainingMinutes = Math.floor((remainingSeconds % 3600) / 60);
    remainingMinutes = remainingMinutes < 10 ? '0' + remainingMinutes : remainingMinutes;
    var remainingSeconds = remainingSeconds % 60;
    remainingSeconds = remainingSeconds < 0 ? '0' + remainingSeconds : remainingSeconds;
    var remainingTime = `学习倒计时\n ${remainingDays}天${remainingHours}小时${remainingMinutes}分钟${remainingSeconds}秒`;
    return remainingTime
};
// 定义需要传递的参数
// var timerConfig = {
//     future: new Date(Date.now() + 9 * 24 * 60 * 60 * 1000)
// };

// 每秒钟更新一次剩余时间
setInterval(function () {
    // 计算剩余时间
    var remainingTime = getCountDown('2023-6-22 18:00:00');

    // 更新元素内容
    document.getElementById('fTime').textContent = remainingTime;
}, 1000);


// 下面用来实现打字机效果

/* document.addEventListener('DOMContentLoaded', () => {
    // your code here


    let wel = document.querySelector('.wel');
    let chars = wel.textContent.split('');

    for (let i = 0; i < chars.length; i++) {
        console.log("打字机");
        let char = chars[i];
        let span = document.createElement('span');
        span.textContent = char;
        wel.appendChild(span);
        span.addEventListener('animationend', () => {
            let nextSpan = span.nextElementSibling;
            if (nextSpan) {
                nextSpan.style.animation = 'blink 1s infinite';
                setTimeout(() => {
                    span.style.color = '#000';
                    span.nextElementSibling.style.opacity = 1;
                }, 100); /* 0.1s 等待下划线消失, 切换颜色和显示下划线 
            } else {
                span.style.color = '#000';
                span.previousElementSibling.style.opacity = 1;
            }
        });
    }

    wel.addEventListener('animationend', () => {
        wel.style.overflow = 'unset'; /* 显示后取消文本裁剪 
    });

})      
*/