import {createStore} from "vuex";
import {userModule} from "@/store/userModule";
import {navbarModule} from "@/store/navbarModule";

export default createStore({
    state: {
        isAuth: false,
    },
    modules: {
        user: userModule,
        navbar: navbarModule
    }
})