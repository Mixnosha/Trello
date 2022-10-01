from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from boardsApp.views import BoardsModelView


boardView = BoardsModelView.as_view({
    'get': 'list',
})
router = DefaultRouter()
router.register(r'board', BoardsModelView, basename='model_work')

urlpatterns = format_suffix_patterns([
    path('get_boards/<int:id>/', boardView, name='board_view'),
])

urlpatterns += router.urls