from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('createcontactlist/', include('createcontactlist.urls'),
         name='createcontactlist'),
    path('domainfinder/', include('domainfinder.urls'), name='domainfinder'),
]
