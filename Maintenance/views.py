from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,View, CreateView
from .models import MaintenanceDB
from django.urls import  reverse_lazy
from .forms import MaintenanceForm
from .filters import Maintenancefilter
# Create your views here.

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



class MaintenanceHomePage(ListView):
    template_name = 'Maintenance/maintenance_page.html'
    queryset = MaintenanceDB.objects.all()
    context_object_name = 'main_all'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = Maintenancefilter(self.request.GET, queryset=self.queryset)
        return context

class MaintenanceDetailView(DetailView):
    queryset = MaintenanceDB.objects.all()
    template_name = 'Maintenance/maintenance_detail.html'
    context_object_name = 'maintenance_detail'



class MaintenanceCreate(CreateView ):
    template_name = 'Maintenance/maintenance_new.html'
    form_class = MaintenanceForm
    model = MaintenanceDB
    success_url = reverse_lazy('maintenance')

    def from_valid(self, form):
        self.object = form.save(commit = True)
        self.object = save()
        return super().form_valid(form)

class MaintenanceDeleteView(DeleteView):
    template_name = 'Maintenance/maintenance_confirm_delete.html'
    model = MaintenanceDB
    success_url = reverse_lazy('maintenance')


class MaintenanceUpdateView(UpdateView):
    template_name = 'Maintenance/maintenance_update.html'
    model = MaintenanceDB
    success_url = reverse_lazy('maintenance')
    fields = "__all__"
#TODO update the view to show the date time selector


def maintenance_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    maintenance = get_object_or_404(MaintenanceDB, pk=pk)

    template_path = 'Maintenance/maintenance_pdf.html'
    context = {'maintenance':maintenance}
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



