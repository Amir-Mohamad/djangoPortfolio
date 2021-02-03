from django import forms


class ContactUsForm(models.ModelForm):
    class Meta:
        model = ContactUsModel
        fields = ('name', 'email', 'phone', 'message')