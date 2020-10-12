from django.urls import path
from . import views

urlpatterns = [
path('Jobs/', views.JobsHomePage.as_view(), name='jobs')
]
