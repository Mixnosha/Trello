from django.contrib import admin
from django.urls import path, include
from .jasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('authUser.urls')),
    path('api/v1/', include('workSpacesApp.urls')),

]

urlpatterns += doc_urls
