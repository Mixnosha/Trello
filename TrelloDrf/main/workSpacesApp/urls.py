from rest_framework.routers import DefaultRouter

from workSpacesApp.views import WorkspaceModelView

router = DefaultRouter()
router.register(r'workspace', WorkspaceModelView, basename='model_work')
urlpatterns = [

]

urlpatterns += router.urls
