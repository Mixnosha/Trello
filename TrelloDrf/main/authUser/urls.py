from django.urls import path, include
from authUser.views import Register, UserStatus

urlpatterns = [
    path('register', Register.as_view()),
    path('user_status', UserStatus.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
