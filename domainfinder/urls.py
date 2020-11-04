from django.urls import path
from . import views
urlpatterns = [
    path('', views.domainfinder, name='domainfinder'),
    path('finddomains/', views.finddomains, name='finddomains'),
]
