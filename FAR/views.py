from django.views.generic import TemplateView,ListView, DetailView, View, CreateView

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import  login_required
from django.urls import  reverse_lazy
from . import models
from .forms import FarForm
# Create your views here.


class FarListView(ListView):
    template_name = 'FAR/far_page.html'
    queryset = models.FAR_DB.objects.all()
    context_object_name = 'far_1'


class FarDetailView(DetailView):
    template_name = 'FAR/far_detail.html'
    queryset = models.FAR_DB.objects.all()
    context_object_name = 'far_detail'

class FarCreateView(CreateView):
    template_name = 'FAR/far_new.html'
    form_class = FarForm
    model = models.FAR_DB
    success_url = reverse_lazy('far')

    def from_valid(self,form):
        self.object = form.save(commit = True)
        self.object = save()
        return super().form_valid(form)




