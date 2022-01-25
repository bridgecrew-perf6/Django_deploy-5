from django.urls import path
from .views import HomeView, ListaContatoView, hello

urlpatterns = [
    path('hello', hello, name='hello-world'),
    path('', HomeView.as_view(), name='home'),
    path('contato', ListaContatoView.as_view(), name='pessoa.index'),
]
