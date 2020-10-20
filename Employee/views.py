from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DeleteView, View, DetailView, CreateView
from . import models
from django.urls import reverse_lazy
from .forms import *
# Create your views here.

class EmployeeHomePage(ListView):
    template_name = 'Employee/employee_home_page.html'
    queryset = models.EmployeeDB.objects.all()
    context_object_name = 'emp_all'

class EmployeeDetail(DetailView):
    model = models.EmployeeDB
    template_name = 'Employee/employee_detail.html'
    context_object_name = 'emp_detail'


class EmployeeCreate(CreateView):
    template_name = 'Employee/employee_new.html'
    form_class = EmployeeFormNew
    model = models.EmployeeDB
    success_url = reverse_lazy('employee')

    def from_valid(self,form):
        self.object = form.save(commit=False)
        self.object = save()
        return super().from_valid(form)

class EmployeeDelete(DeleteView):
    template_name = 'Employee/employee_confirm_delete.html'
    model = models.EmployeeDB
    success_url = reverse_lazy('employee')


