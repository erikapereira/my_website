from django.conf import settings
from django.db import models
from django.utils import timezone


class Contact (models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    text = models.TextField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)


