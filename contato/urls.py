from django.urls import path
from .views import HomeView, hello 

urlpatterns = [
    path('hello', hello, name='hello-world'),
    path('', HomeView.as_view(), name='home'),
]
