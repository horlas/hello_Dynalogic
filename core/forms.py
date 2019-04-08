from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,
                           help_text='Saisissez votre nom')
    email = forms.EmailField(
        help_text="Saisissez votre email"
    )
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea,
        help_text="Saisissez votre message")
