#from django.shortcuts import render
from django.http import HttpResponse


def index(requests):
    return HttpResponse('<h1>Óla Mundo</h1><br><h2>Bonjour Monde</h2>')
