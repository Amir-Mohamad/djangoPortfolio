from django.contrib import admin
from .models import ContactUsModel


@admin.register(ContactUsModel)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    list_filter = ('name', 'phone')