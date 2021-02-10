from django.views.generic import TemplateView,ListView, DetailView, View, CreateView, DeleteView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import  login_required
from django.urls import  reverse_lazy
from . import models
from .forms import FarForm
from .filters import FARfilter
from django import forms
# Create your views here.

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



class FarListView(ListView):
    template_name = 'FAR/far_page.html'
    context_object_name = 'far_1'
    queryset = models.FAR_DB.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = FARfilter(self.request.GET, queryset=self.queryset)
        return context


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

class FarDeleteView(DeleteView):
    model = models.FAR_DB
    success_url = reverse_lazy('far')
    template_name = 'FAR/far_confirm_delete.html'

class FarUpdateView(UpdateView):
    model = models.FAR_DB
    fields = '__all__'
    template_name = 'FAR/far_update.html'
    success_url = reverse_lazy('far')


def FAR_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    far = get_object_or_404(models.FAR_DB, pk=pk)

    template_path = 'FAR/far_pdf.html'
    context = {'far':far}
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

