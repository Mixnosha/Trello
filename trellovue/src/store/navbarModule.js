export const navbarModule = {
    state: () => ({
        profileMenu: false,
        workspaces: [],
        wk__visible: false,
    }),
    getters: {},
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