from django.urls import path 
from receiveship import views



urlpatterns = [
    
  path('', views.case_list, name = 'case_list'),  
  path('case_detail/<int:pk>/', views.case_detail, name = 'case_detail'),
  path('case_create/', views.case_create, name = 'case_create'), 
  path('case_update/<int:pk>/', views.case_update, name = 'case_update') , 
  path('case_delete/<int:pk>/', views.case_delete, name = 'case_delete'),  
   path('record/<int:pk>/', views.record, name = 'record'),  
    
    
    
    
]