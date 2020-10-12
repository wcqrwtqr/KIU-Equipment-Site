from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeHomePage.as_view(), name='employee'),
]
