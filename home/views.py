from django.shortcuts import render
from .forms import ContactForm
from django.utils import timezone
from django.core.mail import mail_admins


def home(request):
    return render(request, 'home.html', {})

def about(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form = form.save()
            form.date_sent = timezone.now()
            form.save()
            mail_admins(
                'You have received a',
                'message',
                fail_silently=False,
            )
            return render(request, "sent.html")

    else:
        form = ContactForm()
        # needs to jump to contact section

    return render(request, "about.html", {'form': form})


# send email separate to about - cannot be dependent on this bit!
# if email doesnt send - error notification.


def portfolio (request):
    return render(request, 'portfolio.html', {})

def sent (request):
    return render(request, 'sent.html')


