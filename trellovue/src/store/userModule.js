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
        setEmail(state, email){
            state.email = email
        }
    },
    actions: {
        Login({state, commit}) {
            Cookies.set('username', state.username, { expires: 90 })
            axios.post('http://192.168.100.6:8000/api/v1/auth/token/login', {
                password: state.password,
                username: state.username
            }).then(res => {
                commit('setToken', res.data.auth_token)
                Cookies.set('token', state.token, { expires: 90 })

            })
        }
    },
    namespaced: true
}