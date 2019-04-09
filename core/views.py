from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from core.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# Create your views here.

class AccueilView(TemplateView, SuccessMessageMixin):

    template_name = "core/index.html"

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)


class ContactView(FormView, SuccessMessageMixin):
    template_name = "core/index.html"
    form_class = ContactForm
    # success_message = "votre message m'est bien parvenu"
    success_url = '.'

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')

            if name and email and message:
                try:
                    message = "{} has sent you a new message:\n\n{}".format(name,message)
                    send_mail('Nouveau contact', message, email, ['aurelia.gourbere@gmail.com'])
                except BadHeaderError:
                    print('error')
                    messages.error(self.request, ('Entete invalide'))
                    return redirect(reverse_lazy('core:home'))
                messages.success(self.request, ("Merci pour votre message"))
                return redirect(reverse_lazy('core:home'))
            else:
                print('yes')
                messages.info(self.request, ('message vide'))
                return redirect(reverse_lazy('core:home'))

        else :
            print('No')
            messages.error(self.request, ('Votre message est invalide'))
            return render(request, self.template_name, self.get_context_data(form=form))


# def form_valid(self, form):
#         sender_name = form.cleaned_data['name']
#         sender_email = form.cleaned_data['email']
#         message = "{} has sent you a new message:\n\n{}".format(sender_name, form.cleaned_data['message'])
#         send_mail('Nouveau contact', message, sender_email, ['aurelia.gourbere@gmail.com'])
#         # print(form.cleaned_data['email'])
#         return super(AccueilView, self).form_valid(form)




