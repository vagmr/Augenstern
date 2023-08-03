//插件制作
export const obj = {
    install(V) {
        //定义全局指令
        V.directive('showInfo', {
            bind(el, binding) {
                console(el.value, binding)
            }
        })
    }
}