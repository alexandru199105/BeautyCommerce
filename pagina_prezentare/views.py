from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, UpdateView, DeleteView, CreateView,FormView


# Create your views here.
def home(request):
    return render(request, 'index.html')


#class MembruCreateView(FormView):
    #template_name = 'pagina_prezentare/'