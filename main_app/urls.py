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
    path('users/<int:user_id>/add_phone/', views.add_phone, name='add_phone'),
    # path('users/<int:user_id>/phones/<int:pk>/delete/', views.PhoneDelete.as_view(), name='phone_delete'),
    path('users/<int:user_id>/phones/<int:phone_id>/delete/', views.remove_phone, name='remove_phone'),
    path('meals/', views.MealList.as_view(), name='meals_index'),
    path('meals/<int:pk>/', views.MealDetail.as_view(), name='meals_detail'),
    path('meals/create/', views.MealCreate.as_view(), name='meals_create'),
    path('meals/<int:pk>/update/', views.MealUpdate.as_view(), name='meals_update'),
    path('meals/<int:pk>/delete/', views.MealDelete.as_view(), name='meals_delete'),
    path('users/<int:user_id>/assoc_meal/<int:meal_id>/', views.assoc_meal, name='assoc_meal'),
    path('users/<int:user_id>/deassoc_meal/<int:meal_id>/', views.deassoc_meal, name='deassoc_meal'),
    path('users/<int:user_id>/add_photo/', views.add_photo, name='add_photo'),
]