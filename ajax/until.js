const BaseUrl = 'http://localhost:3000';
const getSum = num => { num.reduce((a, b) => a + b, 0) };
export default {
    url: BaseUrl,
    fn: getSum,
}