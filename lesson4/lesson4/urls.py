from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_lesson4.urls')),
    path('', include('app_lesson_4.urls')),
    path('myauth/', include('app_auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT)