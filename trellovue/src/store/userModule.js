import axios from 'axios';

export const userModule = {
    state: () => ({
        username: '',
        password: '',
        token: '',

    }),
    getters: {

    },
    mutations: {
        setUsername(state, username) {
            state.username = username;
        },
        setPassword(state, password){
            state.password = password
        },
        setToken(state, token){
            state.token = token
        },
    },
    actions: {
        Login({state, commit}){
            console.log(state.password)
            console.log(state.username)
            axios.post('http://192.168.100.6:8000/api/v1/auth/token/login', {
                password: state.password,
                username: state.username
            }).then(res => {
                commit('setToken', res.data.auth_token)
            })
        }
    },
    namespaced: true
}