import { createApp } from 'vue'
import App from './App.vue'
import router from './router/router'
import components from '@/components/UI';
import componentHomeWk from '@/components/HomeWK';
import store from '@/store';
import directives from '@/directives';


const app = createApp(App)

components.forEach(component => {
    app.component(component.name, component)
})

components.forEach(componentHomeWk => {
    app.component(componentHomeWk.name, componentHomeWk)
})


directives.forEach(directive => {
    app.directive(directive.name, directive)
})

app
    .use(router)
    .use(store)
    .mount('#app')