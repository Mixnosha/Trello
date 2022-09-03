import axios from "axios";
import Cookies from "js-cookie";

export const navbarModule = {
    state: () => ({
        profileMenu: false,
        workspaces: [],
        wk__visible: false,
    }),
    actions: {
        async loadWk(state){
               const res = await axios.get('http://127.0.0.1:8000/api/v1/workspace/', {
                    headers: {
                        'Authorization': `Token ${Cookies.get('token')}`
                    }
                })
                state.commit('setWorkspaces', res.data)
        },
    },
    mutations: {
        setProfileMenu(state, profileMenu) {
            state.profileMenu = profileMenu;
        },
        setWk__visible(state, visible) {
            state.wk__visible = visible;
        },
        setWorkspaces(state, workspaces){
            state.workspaces = workspaces
        }
    },
    namespaced: true
}