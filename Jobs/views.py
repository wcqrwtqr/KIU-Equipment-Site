from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView,ListView,DetailView, View, CreateView, DeleteView, UpdateView
from .models import JobsDB, JobMasterInfo
from django.contrib.auth.decorators import login_required
from django.urls import  reverse_lazy
from .forms import *
from .import models
from .filters import Jobsfilter
# Create your views here.


class JobsHomePage(ListView):
    template_name = 'Jobs/jobs_page.html'
    queryset = JobsDB.objects.all()
    context_object_name = 'jobs_all'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = Jobsfilter(self.request.GET, queryset=self.queryset)
        return context

class JobsDetailView(DetailView):
    queryset = JobsDB.objects.all()
    context_object_name = 'jobs_detail'
    template_name = 'Jobs/jobs_detail.html'

class JobsCreate(CreateView ):
    template_name = 'Jobs/jobs_new.html'
    form_class = JobsForm
    model = models.JobsDB
    success_url = reverse_lazy('jobs')

    def from_valid(self, form):
        self.object = form.save(commit = True)
        self.object = save()
        return super().form_valid(form)

class JobsDeleteView(DeleteView):
    template_name = 'Jobs/jobs_confirm_delete.html'
    model = models.JobsDB
    success_url = reverse_lazy('jobs')

class JobsUpdateView(UpdateView):
    template_name = 'Jobs/jobs_update.html'
    model = models.JobsDB
    success_url = reverse_lazy('jobs')
    fields = "__all__"

class JobsMasterInfoView(DetailView):
    queryset = JobMasterInfo.objects.all()
    context_object_name = 'jobs_master_info'
    template_name = 'Jobs/jobs_master_info.html'
