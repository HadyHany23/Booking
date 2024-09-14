from django.urls import path
from . import views
from .views import user_list_view,add_user_view

urlpatterns = [
    path('', views.home, name='home'), 
    path('login/', views.login_view, name='login'),
    path('admin/add-user/', add_user_view, name='add_user'),
    path('admin/user-list/', user_list_view, name='user_list'),

]
