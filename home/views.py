from django.shortcuts import render
from .forms import ContactForm

def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})
    form = ContactForm()
    # fix this bit!
    # make html work D:
