from rest_framework.routers import DefaultRouter

from columnApp.views import ColumnModelRetrieve

router = DefaultRouter()
router.register(r'columns_get', ColumnModelRetrieve, basename='column_model')

urlpatterns = [

]


urlpatterns += router.urls