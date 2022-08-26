export const navbarModule = {
    state: () => ({
        profileMenu: false
    }),
    getters: {},
    mutations: {
        setProfileMenu(state, profileMenu) {
            state.profileMenu = profileMenu;
        },
    },
    namespaced: true
}