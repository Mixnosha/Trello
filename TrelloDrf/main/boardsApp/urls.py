from rest_framework.routers import DefaultRouter

from boardsApp.views import BoardsModelView

router = DefaultRouter()
router.register(r'board', BoardsModelView, basename='board_work')
urlpatterns = [

]

urlpatterns += router.urls
