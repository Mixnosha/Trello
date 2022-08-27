export const navbarModule = {
    state: () => ({
        profileMenu: false,
        workspaces: []
    }),
    getters: {},
    mutations: {
        setProfileMenu(state, profileMenu) {
            state.profileMenu = profileMenu;
        },
        setWorkspaces(state, workspaces){
            state.workspaces = workspaces
        }
    },
    namespaced: true
}