from django.contrib import admin
from django.urls import path, include
from .jasg import urlpatterns as doc_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('authUser.urls')),
    path('api/v1/', include('workSpacesApp.urls')),
    path('api/v1/', include('commentApp.urls'))

]

urlpatterns += doc_urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
