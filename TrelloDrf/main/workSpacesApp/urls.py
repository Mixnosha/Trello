from rest_framework.routers import DefaultRouter

from workSpacesApp.views import WorkSpacesView

router = DefaultRouter()
router.register(r'workspace', WorkSpacesView, basename='workspace')
urlpatterns = [

]

urlpatterns += router.urls
