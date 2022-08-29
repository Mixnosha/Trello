import axios from 'axios';
import Cookies from "js-cookie";

export const userModule = {
    state: () => ({
        username: '',
        password: '',
        token: '',
        email: '',

    }),
    getters: {},
    mutations: {
        setUsername(state, username) {
            state.username = username;
        },
        setPassword(state, password) {
            state.password = password
        },
        setToken(state, token) {
            state.token = token
        },
        setEmail(state, email) {
            state.email = email
        }
    },
    actions: {
        async Login({state, commit}) {
            Cookies.set('username', state.username, {expires: 90})
            const res = await axios.post('http://127.0.0.1:8000/api/v1/auth/token/login', {
                password: state.password,
                username: state.username
            })
            console.log(res.data)
            commit('setToken', res.data.auth_token)
            Cookies.set('token', state.token, {expires: 90})
        }
    },
    namespaced: true
}