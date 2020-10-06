from django.urls import path
from . import views

urlpatterns = [
path('Jobs/', views.JobsList.as_view(), name='jobs')
]
