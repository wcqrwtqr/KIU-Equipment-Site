from django.urls import path
from . import views

urlpatterns = [
    path('', views.MaintenanceHomePage.as_view(), name='maintenance'),
    path('maintenance/<int:pk>', views.MaintenanceDetailView.as_view(), name='maintenance_detail'),
    path('maintenance/<int:pk>/delete', views.MaintenanceDeleteView.as_view(), name='maintenance_delete'),
    path('maintenance/new/', views.MaintenanceCreate.as_view(), name='maintenance_new'),
]
