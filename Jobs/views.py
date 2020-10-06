from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class JobsList(TemplateView):
    template_name = 'jobs/Jobs_page.html'
