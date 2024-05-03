from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/list/', views.user_list, name='user_list'),
    path('user/create/', views.user_create, name='user_create'),
    path('user/update/<int:pk>/', views.user_update, name='user_update'),
    path('user/delete/<int:pk>/', views.user_delete, name='user_delete'),
    path('reservation/list/', views.reservation_list, name='reservation_list'),
    path('reservation/create/', views.reservation_create, name='reservation_create'),
    path('reservation/update/<int:pk>/', views.reservation_update, name='reservation_update'),
    path('reservation/delete/<int:pk>/', views.reservation_delete, name='reservation_delete'),
]
