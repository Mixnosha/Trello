import axios from "axios";
import Cookies from "js-cookie";

export const oneWk = {
    state: () => ({
        wk: {
            title: '',
            logo: '',
            status: {
                title: '',
                description: '',
            },
            description: '',
            slug: '',
            web_site: '',
        },
        id: ''
    }),
    actions: {
        async loadWk({state, commit}) {
            const res = await axios.get(`http://127.0.0.1:8000/api/v1/workspace/${state.id}`, {
                headers: {
                    'Authorization': `Token ${Cookies.get('token')}`
                }
            })
            commit('setWkTitle', res.data.title)
            commit('setWkLogo', res.data.logo)
            commit('setWkStatus', res.data.status)
            commit('setWkDescription', res.data.description)
            commit('setWkSlug', res.data.slug)
            commit('setWkWeb_site', res.data.web_site)
        },
    },
    mutations: {
        setWk(state, wk) {
            state.wk = wk;
        },
        setWkTitle(state, title){
            state.wk.title = title
        },
        setWkLogo(state, logo){
            state.wk.logo = logo
        },
        setWkStatus(state, status){
            state.wk.status = status
        },
        setWkDescription(state, description){
            state.wk.description = description
        },
        setWkSlug(state, slug){
            state.wk.slug = slug
        },
        setWkWeb_site(state, web_site){
            state.wk.web_site = web_site
        },
        setWkId(state, id){
            state.id = id
        },
    },
    namespaced: true
}