from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
import djoser
from authUser.views import Register, Login, UserStatus

urlpatterns = [
    path('register', Register.as_view()),
    path('login', Login.as_view()),
    path('user_status', UserStatus.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
