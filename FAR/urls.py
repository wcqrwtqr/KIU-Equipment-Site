from django.urls import path
from . import views

#app_name = 'FAR'

urlpatterns = [
    path('', views.Far_List.as_view(), name='far'),
]
