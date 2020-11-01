from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobsHomePage.as_view(), name='jobs'),
    path('jobs/<int:pk>', views.JobsDetailView.as_view(), name='jobs_detail'),
    path('jobs/new/', views.JobsCreate.as_view(), name='jobs_new'),
    path('jobs/<int:pk>/update/', views.JobsUpdateView.as_view(), name='jobs_update'),
    path('jobs/<int:pk>/delete/', views.JobsDeleteView.as_view(), name='jobs_delete'),
    path('jobs/master_info/<int:pk>', views.JobsMasterInfoView.as_view(), name='jobs_master_info'),
    # path('pdf/', views.render_pdf_view, name='test-view'),
    path('pdf/<int:pk>', views.job_render_pdf_view, name='pdf_job_view'),
]
