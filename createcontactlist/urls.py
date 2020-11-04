from django.urls import path
from . import views
urlpatterns = [
    path('', views.createcontactlist, name='createcontactlist'),
    path('loginlinkedin/', views.loginlinkedin, name='loginlinkedin'),
    path('applyfilter/', views.applyfilter, name='applyfilter'),
    path('linkedindatascrap/', views.linkedindatascrap, name='linkedindatascrap'),
    path('datascrapeddwnld/', views.datascrapeddwnld, name='datascrapeddwnld'),
]
