from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class JobsList(TemplateView):
    template_name = 'Jobs/jobs_page.html'
