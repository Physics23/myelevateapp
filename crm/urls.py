
from django.urls import path
from .  import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('register/', views.register, name ='register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('createclient/', views.createclient, name ='createclient'),
    path('education/', views.education, name = 'education'),
    path('updateclient/<int:pk>', views.updateClient, name = 'updateclient'),
    path('client_detail/<int:pk>/', views.client_detail, name = 'client_detail'),
    path('client_delete/<int:pk>/', views.client_delete, name = 'client_delete'),
]
