from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DeleteView, View, DetailView
from . import models
# Create your views here.

class EmployeeHomePage(ListView):
    template_name = 'Employee/employee_home_page.html'
    queryset = models.EmployeeDB.objects.all()
    context_object_name = 'emp_all'

class EmployeeDetail(DetailView):
    model = models.EmployeeDB
    template_name = 'Employee/employee_detail.html'
    context_object_name = 'emp_detail'
