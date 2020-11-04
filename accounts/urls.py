from django.urls import path, include
from . import views
# from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path('', views.indexView, name="home"),
    path('', views.dashboardView, name="dashboard"),
    path('createcontactlist/', include('createcontactlist.urls'),
         name='createcontactlist'),
    path('domainfinder/', include('domainfinder.urls'), name='domainfinder'),
    path('emailvalidation/', include('emailValidation.urls'), name='emailvalidation'),
    # path('login/', LoginView.as_view(), name="login_url"),
    # path('register/', views.registerView, name="register_url"),
    # path('logout/', LogoutView.as_view(next_page='dashboard'), name="logout"),

]
