from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ["name", "email", 'message']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': "Name"}),
            'email': forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': "Email"}),
            'message': forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': "Message"}),


        }








