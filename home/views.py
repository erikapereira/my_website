from django.shortcuts import render
from .forms import ContactForm

def home(request):
    return render(request, 'home.html', {})

def about(request):
    # form = ContactForm()
    # return render(request, 'about.html', {'form': form})

    context = {}
    context['form'] = ContactForm()
    return render(request, "about.html", context)

def portfolio (request):
    return render(request, 'portfolio.html', {})



