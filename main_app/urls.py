from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('users/', views.users_index, name='index'),
    path('users/<int:user_id>/', views.users_detail, name='detail'),
    path('users/create/', views.UserCreate.as_view(), name='users_create'),
    path('users/<int:pk>/update', views.UserUpdate.as_view(), name='users_update'),
    path('users/<int:pk>/delete', views.UserDelete.as_view(), name='users_delete'),
    path('user/<int:user_id>/add_phone/', views.add_phone, name='add_phone'),
]