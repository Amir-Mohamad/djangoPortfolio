from django import forms
from .models import ContactUsModel

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUsModel
        fields = ('name', 'email', 'phone', 'message')
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control", "id":"name","placeholder": "Name","data-validation-required-message":"Please enter your name."}),
            'phone': forms.TextInput(attrs={"class": "form-control", "id":"phone", "placeholder": "Phone", "data-validation-required-message":"Please enter your phone"}),
            'email': forms.TextInput(attrs={"class": "form-control", "id":"email", "placeholder": "Email", "data-validation-required-message":"Please enter your email"}),
            'message': forms.TextInput(attrs={"class": "form-control", "id":"message","placeholder": "Message.", "data-validation-required-message":"Please enter your Message"}),
        }
            
