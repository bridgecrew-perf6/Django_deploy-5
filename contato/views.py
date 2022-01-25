from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Contato


class HomeView(TemplateView):
    template_name = 'contato/index.html'


class ListaContatoView(ListView):
    model = Contato
    queryset = Contato.objects.all().order_by('nome_completo')


def hello(requests):
    return HttpResponse('<h1>Óla Mundo</h1><br><h2>Bonjour Monde</h2>')

