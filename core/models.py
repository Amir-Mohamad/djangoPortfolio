from django.db import models


class ContactUsModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ---> {self.email}'