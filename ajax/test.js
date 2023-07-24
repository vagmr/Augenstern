const fs = require('fs');
fs.writeFile('first.txt', "hello world", err => {
    if (err) console.log(err);
    else console.log("文件写入成功");
})
fs.readFile('first.txt', (err, data) => {
    if (err) console.log(err);
    else console.log(data.toString());
})