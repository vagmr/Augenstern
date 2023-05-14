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
    addres: lundon,
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
function getRandom(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min; //含最大值，含最小值
}
var ranNum = getRandom(0, 50);
var count = 0;
while (count <= 4) {
    var num = prompt('猜0-50之间的一个数字')
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