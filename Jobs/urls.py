from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobsHomePage.as_view(), name='jobs'),
    path('jobs/<int:pk>', views.JobsDetailView.as_view(), name='jobs_detail'),
    path('jobs/master_info/<int:pk>', views.JobsMasterInfoView.as_view(), name='jobs_master_info'),
]
