from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from core.forms import ContactForm
from django.core.mail import send_mail
# Create your views here.


class AccueilView(FormView, SuccessMessageMixin):
    template_name = "core/index.html"
    form_class = ContactForm
    success_message = "votre message m'est bien parvenu"
    success_url = '.'

    def form_valid(self, form):
        sender_name = form.cleaned_data['name']
        sender_email = form.cleaned_data['email']
        message = "{} has sent you a new message:\n\n{}".format(sender_name, form.cleaned_data['message'])
        send_mail('Nouveau contact', message, sender_email, ['aurelia.gourbere@gmail.com'])
        # print(form.cleaned_data['email'])
        return super(AccueilView, self).form_valid(form)




