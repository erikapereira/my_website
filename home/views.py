from django.shortcuts import render
from .forms import ContactForm
from django.utils import timezone


def home(request):
    return render(request, 'home.html', {})

def about(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form = form.save()
            form.date_sent = timezone.now()
            form.save()
            




    form = ContactForm
    return render(request, "about.html", {'form' : form})



def portfolio (request):
    return render(request, 'portfolio.html', {})



