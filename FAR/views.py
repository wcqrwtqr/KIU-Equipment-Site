from django.views.generic import TemplateView,ListView, DetailView, View, CreateView
from django.shortcuts import render, get_object_or_404, redirect
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
    #redirect_field_name = 'FAR/far_detail.html'



#def addFar(request, pk):
#    far = get_object_or_404(models.FAR_DB, pk=pk )
#   if request.method == "POST":
#       form = FarForm(request.POST)
#       if form.is_valid():
#           far = form.save(commit=False)
#           comment.far = far
#           comment.save()
#       return redirect('far', pk=far.pk)
#   else:
#       form = FarForm()
#   return render(request, 'FAR/far_page.html', {'form': form})



def addFar(request):
    form= FarForm(request.POST or None)
    if form.is_valid():
        form.addFar()
        form.save()
        
        context= {'form': form }

    return render(request, 'FAR/far_page.html', context)

