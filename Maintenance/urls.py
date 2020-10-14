from django.urls import path
from . import views

urlpatterns = [
    path('', views.MaintenanceHomePage.as_view(), name='maintenance'),
    path('maintenance/<int:pk>', views.MaintenanceDetailView.as_view(), name='maintenance_detail'),
]
