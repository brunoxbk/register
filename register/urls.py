from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from .api import CustomAuthToken, RegisterView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cashbook/', include('cashbook.urls')),
    path('auth/login/', CustomAuthToken.as_view()),
    path('auth/register/', RegisterView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
