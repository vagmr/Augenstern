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
