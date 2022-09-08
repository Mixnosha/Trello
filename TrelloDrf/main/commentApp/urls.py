from rest_framework.routers import DefaultRouter

from commentApp.views import StatusAllView

router = DefaultRouter()
router.register(r'status', StatusAllView, basename='status_model')
urlpatterns = [

]

urlpatterns += router.urls
