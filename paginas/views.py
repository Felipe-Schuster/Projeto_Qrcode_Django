from django.shortcuts import render
from django.views.generic import TemplateView

# criar uma classe templats
class IndexView(TemplateView):
    template_name = 'paginas/index.html'
    
class BaseView(TemplateView):
    template_name ='paginas/base.html'