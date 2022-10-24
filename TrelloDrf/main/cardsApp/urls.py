from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from cardsApp.views import CardsCRUD


cardView = CardsCRUD.as_view({
    'get': 'list',
})
router = DefaultRouter()
router.register(r'card', CardsCRUD, basename='card')

urlpatterns = format_suffix_patterns([
    path('get_cards/<int:id>/', cardView, name='card_view'),
])

urlpatterns += router.urls

