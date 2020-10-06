from django.urls import path
from . import views

urlpatterns = [
path('', views.MaintenanceList.as_view(), name='maintenance')
]
