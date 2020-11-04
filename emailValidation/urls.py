from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.emailvalidation, name='emailvalidation'),
    path('singlemailvalidation/', views.singlemailvalidation,
         name='singlemailvalidation'),
    path('multiplemailvalidation/', views.multiplemailvalidation,
         name='multiplemailvalidation'),
    path('upload_csv/', views.upload_csv, name='upload_csv'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
