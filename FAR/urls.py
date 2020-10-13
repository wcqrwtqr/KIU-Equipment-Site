from django.urls import path
from . import views
#app_name = 'FAR'

urlpatterns = [
    path('far/<int:pk>', views.FarDetailView.as_view(), name='far_detail'),
    path('', views.FarListView.as_view(), name='far'),
]
