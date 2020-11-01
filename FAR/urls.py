from django.urls import path
from . import views

urlpatterns = [
    path('far/<int:pk>', views.FarDetailView.as_view(), name='far_detail'),
    path('pdf/<int:pk>', views.FAR_render_pdf_view, name='far_pdf'),
    path('', views.FarListView.as_view(), name='far'),
    path('far/new/', views.FarCreateView.as_view(), name='far_new'),
    path('far/<int:pk>/update/', views.FarUpdateView.as_view(), name='far_update'),
    path('far/<int:pk>/delete/', views.FarDeleteView.as_view(), name='far_delete'),
]
