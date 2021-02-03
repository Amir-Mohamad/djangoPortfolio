from django.shortcuts import render
from .forms import ContactUsForm
from django.views import View


class Home(View):
    template_name = 'core/home.html'
    form_class = ContactUsForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, {'form':form})

        