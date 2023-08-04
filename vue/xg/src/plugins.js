//插件制作
export const obj = {
    install(V) {
        //定义全局指令
        V.directive('focus', {
            inserted(el) {
                el.focus();
            }
        }),
            V.directive('color', {
                inserted(el, banding) {
                    el.style.color = banding.value
                },
                update(el, banding) {
                    el.style.color = banding.value
                }
            }),
            //添加全局指令v-loading
            V.directive('loading', {
                inserted(el, banding) {

                    banding.value ? el.classList.add('loading') : el.classList.remove('loading');
                },
                update(el, banding) {

                    banding.value ? el.classList.add('loading') : el.classList.remove('loading');

                }
            })
    }
}