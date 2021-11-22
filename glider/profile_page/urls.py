from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('', views.personal, name='profile'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('profile/<int:pk>/edit/', views.ProfileUpdateView.as_view(), name='edit_profile'),


]