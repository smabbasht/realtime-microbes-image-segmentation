from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('detect', views.process_image, name='process_image'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
