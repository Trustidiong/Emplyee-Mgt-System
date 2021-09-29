from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.employee_form, name = 'employee_insert'), # GET AND POST REQUEST FOR INSERT OPERATIONS
    path('list/', views.employee_list, name = 'employee_list'), # GET  REQUEST TO RETRIEVE AND DISPLAY RECORDS
    path('<int:id>/', views.employee_form, name = 'employee_update'),# GET AND POST REQUEST FOR UPDATE OPERATIONS
    path('delete/<int:id>/', views.employee_delete, name = 'employee_delete'),# GET AND POST REQUEST FOR DELETE OPERATIONS
]

