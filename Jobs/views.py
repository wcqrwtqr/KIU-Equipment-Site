from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView,ListView,DetailView, View, CreateView, DeleteView, UpdateView
from .models import JobsDB, JobMasterInfo
from django.contrib.auth.decorators import login_required
from django.urls import  reverse_lazy
from .forms import *
from .import models
from .filters import Jobsfilter

# Below are the imports for the xhtml2pdf 
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
# from django.contrib.staticfiles import finders


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




#----------------------------
# making the pdf page
# def render_pdf_view(request):
#     template_path = 'Jobs/jobs_pdf.html'
#     context = {'myvar': 'this is your template context'}
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'filename="report.pdf"'
#     # find the template and render it.
#     template = get_template(template_path)
#     html = template.render(context)

#     # create a pdf
#     pisa_status = pisa.CreatePDF(
#         html, dest=response )
#     # if error then show some funny view
#     if pisa_status.err:
#         return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response

def job_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    job = get_object_or_404(JobsDB, pk=pk)

    template_path = 'Jobs/jobs_pdf.html'
    context = {'job':job}
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






