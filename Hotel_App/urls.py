from django.urls import path
from . import views
from .views import user_list_view,add_user_view

urlpatterns = [
    path('', views.home, name='home'), 
    path('login/', views.login_view, name='login'),
    path('admin/add-user/', add_user_view, name='add_user'),
    path('admin/user-list/', user_list_view, name='user_list'),
    path('admin/user-list/', user_list_view, name='user_list'),
    path('add-hotel', views.add_hotel, name='add_hotel'),
    path('available-hotels', views.Available, name='available'),
    path('add-reservation', views.add_reservation, name='add_reservation'),
    path('Reservations', views.view_reservations, name='view_reservations'),
    path('edit_customer/<int:id>/', views.edit_customer, name='edit_customer'),
    path('delete_customer/<int:id>/', views.delete_customer, name='delete_customer'),
    path('edit_hotel/<int:id>/', views.edit_hotel, name='edit_hotel'),
    path('delete_hotel/<int:id>/', views.delete_hotel, name='delete_hotel'),


]
