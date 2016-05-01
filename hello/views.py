from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def codebase(request):
    return render(request, 'codebase.html')

def dependencies(request):
    return render(request, 'dependencies.html')

def config(request):
    return render(request, 'config.html')

def backing(request):
    return render(request, 'backing-services.html')

def build(request):
    return render(request, 'build-release-run.html')

def process(request):
    return render(request, 'process.html')

def port(request):
    return render(request, 'port-binding.html')

def concurrency(request):
    return render(request, 'concurrency.html')

def disposability(request):
    return render(request, 'disposability.html')

def devprod(request):
    return render(request, 'dev-prod-parity.html')

def logs(request):
    return render(request, 'logs.html')

def admin(request):
    return render(request, 'admin-process.html')
