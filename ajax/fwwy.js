const http = require('http');
const fs = require('fs');
const path = require('path');

const sv = http.createServer();
sv.on('request', (req, res) => {
    if (req.url === '/index.html') {
        fs.readFile(path.join(__dirname, 'node/压缩版本.html'), (err, data) => {
            if (err) console.log(err);
            else {
                res.setHeader('Content-Type', 'text/html;charset=utf-8');
                res.end(data.toString())
                console.log('访问成功');
            }
        })
    }
    else {
        res.setHeader('Content-Type', 'text/html;charset=utf-8');
        console.log('文件路径不存在');
        res.end('404 Not Found')
    }
})
sv.listen(3000, () => {
    console.log('服务器运行中');
})