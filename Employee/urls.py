from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeHomePage.as_view(), name='employee'),
    path('employee/<int:pk>', views.EmployeeDetail.as_view(), name='employee_detail'),
    path('employee/<int:pk>/delete/', views.EmployeeDelete.as_view(), name='employee_delete'),
    path('employee/new/', views.EmployeeCreate.as_view(), name='employee_new'),
]
