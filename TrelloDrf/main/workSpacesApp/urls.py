from rest_framework.routers import DefaultRouter

from workSpacesApp.views import WorkSpacesView, WorkspaceModelView

router = DefaultRouter()
router.register(r'workspace', WorkSpacesView, basename='workspace')
router.register(r'model_work', WorkspaceModelView, basename='model_work')
urlpatterns = [

]

urlpatterns += router.urls
