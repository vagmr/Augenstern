let obj = {
    x: 100
}
let obj2 = {
    y: 100,
}
Object.defineProperty(obj2, 'x', {
    get() {
        return obj.x;
    },
    set(value) {
        obj.x = value;
    }
})
obj2.x = 200;
console.log(obj);
console.log(obj2.x);