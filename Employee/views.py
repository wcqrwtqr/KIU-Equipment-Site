from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DeleteView, View, DetailView, CreateView, UpdateView
from . import models
from django.urls import reverse_lazy
from .forms import *
from .filters import Employeefilter
# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

class EmployeeHomePage(ListView):
    template_name = 'Employee/employee_home_page.html'
    queryset = models.EmployeeDB.objects.all()
    context_object_name = 'emp_all'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = Employeefilter(self.request.GET, queryset=self.queryset)
        return context


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


class EmployeeUpdateView(UpdateView):
    template_name = 'Employee/employee_update.html'
    model = models.EmployeeDB
    success_url = reverse_lazy('employee')
    fields = "__all__"


def employee_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    employee = get_object_or_404(EmployeeDB, pk=pk)

    template_path = 'Employee/employee_pdf.html'
    context = {'employee':employee}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response )
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



