
from django import forms
from .models import  Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'comment']
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Your Name'}),
        'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}),
        'subject': forms.TextInput(attrs={'class': 'form-control','placeholder':'Subject'}),
        'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 5,'placeholder':'Comment'}),
    }