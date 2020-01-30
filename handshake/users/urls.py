from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include

app_name = "users"
urlpatterns = [
    path('',views.index, name = 'index'),
    path('login/',auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    path('signup/', views.signup, name = "signup"),
    path('home/', views.home, name = "home"),
]
