from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobsHomePage.as_view(), name='jobs'),
    path('jobs/<int:pk>', views.JobsDetailView.as_view(), name='jobs_detail'),
]
