const res = require('http');
const sv = res.createServer();
sv.on('request', (req, res) => {
    res.setHeader('content-type', 'text/plain;charset=utf-8')
    res.end('Hello World');
})
sv.listen(3000, () => {
    console.log('服务器后台进行中...');
})