from django.shortcuts import render
import requests
from datetime import datetime, date, time, timedelta

# Create your views here.
def home(request):
        return render(request, "core/home.html")

def about(request):
        return render(request, "core/about.html")

def store(request):
        return render(request, "core/store.html")

def contact(request):
        return render(request, "core/contact.html")

def sample(request):
        return render(request, "core/sample.html")
