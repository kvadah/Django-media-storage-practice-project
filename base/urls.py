from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
urlpatterns = [
    path('', views.getImages, name='get-images'),
    path('upload-image/', views.uploadImage, name='upload-image'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
