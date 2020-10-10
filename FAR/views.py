from django.views.generic import TemplateView,ListView, DetailView, View
from . import models
# Create your views here.

#class Far_List(TemplateView):
#    template_name = 'FAR/far_page.html'


class FarListView(ListView):
    template_name = 'FAR/far_page.html'
    queryset = models.FAR_DB.objects.all()
    context_object_name = 'far_1'







