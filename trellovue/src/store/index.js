import {createStore} from "vuex";
import {userModule} from "@/store/userModule";

export default createStore({
    state: {
        isAuth: false,
    },
    modules: {
        post: userModule
    }
})