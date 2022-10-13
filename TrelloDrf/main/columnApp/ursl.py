from django.urls import path
from rest_framework.routers import DefaultRouter

from columnApp.views import ColumnList, ColumnModelCRUD

router = DefaultRouter()
router.register(r'column', ColumnModelCRUD, basename='column_model' )

urlpatterns = [
   path('column_list/<int:pk>/', ColumnList)
]

urlpatterns += router.urls

