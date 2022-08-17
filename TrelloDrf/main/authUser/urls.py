from django.contrib import admin
from django.urls import path

from authUser.views import Register

urlpatterns = [
    path('register', Register.as_view())

]
