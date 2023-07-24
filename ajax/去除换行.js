const fs = require('fs');
const path = require('path');
let NewStr;
fs.readFile(path.join(__dirname, '测试用例.html'), (err, data) => {
    if (err) console.log(err);
    else {
        let Htmlstr = data.toString();
        NewStr = Htmlstr.replace(/[\r\n]/g, '');
        console.log(NewStr);
        fs.writeFile(path.join(__dirname, '压缩版本.html'), NewStr, err => {
            if (err) console.log(err);
            else console.log('成功');
        })
    }
})
