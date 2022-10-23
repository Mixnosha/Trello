from rest_framework.routers import DefaultRouter
from cardsApp.views import CardsCRUD

router = DefaultRouter()
router.register(r'card', CardsCRUD, basename='card')

urlpatterns = [

]

urlpatterns += router.urls