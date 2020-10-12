from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView, View
from .models import JobsDB
# Create your views here.


class JobsHomePage(ListView):
    template_name = 'Jobs/jobs_page.html'
    queryset = JobsDB.objects.all()
    context_object_name = 'jobs_all'
