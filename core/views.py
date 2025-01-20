from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>OBRIGADO LETICIA, DEU CERTO.</h1>")
