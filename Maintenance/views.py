from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,View, CreateView
from .models import MaintenanceDB
from django.urls import  reverse_lazy
from .forms import MaintenanceForm

# Create your views here.

class MaintenanceHomePage(ListView):
    template_name = 'Maintenance/maintenance_page.html'
    queryset = MaintenanceDB.objects.all()
    context_object_name = 'main_all'

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


