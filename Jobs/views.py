from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView, View
from .models import JobsDB, JobMasterInfo
# Create your views here.


class JobsHomePage(ListView):
    template_name = 'Jobs/jobs_page.html'
    queryset = JobsDB.objects.all()
    context_object_name = 'jobs_all'

class JobsDetailView(DetailView):
    queryset = JobsDB.objects.all()
    context_object_name = 'jobs_detail'
    template_name = 'Jobs/jobs_detail.html'

class JobsMasterInfoView(DetailView):
    queryset = JobMasterInfo.objects.all()
    context_object_name = 'jobs_master_info'
    template_name = 'Jobs/jobs_master_info.html'
