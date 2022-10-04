from django.urls import path
from rest_framework.routers import DefaultRouter

from status.views import StatusAllView

router = DefaultRouter()
router.register(r'status/<str:some>/w', StatusAllView, basename='status_model')  # some == wk or some == br (boards)
urlpatterns = [
    path('status/<str:some>', StatusAllView.as_view({'get': 'list'}))
]

urlpatterns += router.urls
