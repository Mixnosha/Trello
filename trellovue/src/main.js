import { createApp } from 'vue'
import App from './App.vue'
import router from './router/router'

const cors=require("cors");
const corsOptions ={
    origin:'*',
    credentials:true,            //access-control-allow-credentials:true
    optionSuccessStatus:200,
}

createApp(App)
    .use(router)
    // .use(cors(corsOptions))
    .mount('#app')