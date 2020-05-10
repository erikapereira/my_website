from django.db import models
from django.utils import timezone



class Contact (models.Model):
    name = models.CharField(max_length=200, error_messages={'required': "Name is required."})
    email = models.EmailField()
    message = models.TextField(max_length=200)
    date_sent = models.DateTimeField(default=timezone.now)

    def send(self):
        self.save()

    def __str__(self):
        return self.name








