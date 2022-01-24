from re import template
#from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'contato/index.html'


def hello(requests):
    return HttpResponse('<h1>Óla Mundo</h1><br><h2>Bonjour Monde</h2>')
