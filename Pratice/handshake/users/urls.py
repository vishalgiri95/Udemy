from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib.auth.models import User
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = "users"
urlpatterns = [
    path('',views.index, name = 'index'),
    # path('password-reset/',auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html'), name = 'password_reset'),
    # path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'), name = 'password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'), name = 'password_reset_confirm'),
    path('signup/', views.signup, name = "signup"),
    path('home/', views.PostListView.as_view(), name = "home"),  # It looks for the Template <app>_<model>_<viewtype>.html
    path('profile/', views.UserProfile, name = "profile"),
    path('post/<int:pk>/' , PostDetailView.as_view(), name = 'post-detail'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update/' , PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/' , PostDeleteView.as_view(), name = 'post-delete'),
]

