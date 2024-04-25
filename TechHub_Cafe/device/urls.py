from django.urls import path
from . import views

urlpatterns = [
    path('computer/', views.computer_list, name='computer_list'),
    path('computer/create/', views.computer_create, name='computer_create'),
    path('computer/update/<int:pk>/', views.computer_update, name='computer_update'),
    path('computer/delete/<int:pk>/', views.computer_delete, name='computer_delete'),
]