from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DeleteView, View
from . import models

# Create your views here.


class EmployeeHomePage(ListView):
    template_name = 'Employee/employee_home_page.html'
    queryset = models.EmployeeDB.objects.all()
    context_object_name = 'emp_all'

