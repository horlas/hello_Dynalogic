from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from core.forms import ContactForm
from django.core import mail


class HomeViewTest(TestCase):

    def test_view(self):
        client = Client()
        response = client.get(reverse('core:home'))
        # test response
        self.assertEqual(response.status_code, 200)
        # test if the form is present
        self.assertIsInstance(response.context['form'], ContactForm)
        # test the template used
        self.assertTemplateUsed(response, 'core/index.html')
        # test the integrity of html
        self.assertContains(response,  '<a class="navbar-brand js-scroll-trigger" href="#page-top">Aurélia Gourbère</a>', html=True)

    def test_contact_form(self):
        data = {'nom':'Mister Oizo',
                'email':'toto@gmail.com',
                'message':'je ne veux que ton bien'}
        client = Client()
        response = client.post(reverse('core:message'), data, follow=True)

        self.assertRedirects(
            response,
            expected_url=reverse('core:home'),
            status_code=302,
            target_status_code=200
        )
        # test the success message
        self.assertContains(response, 'Merci pour votre message')

        # check if the mail is well sent
        self.assertEqual(len(mail.outbox), 1)
        # grab uid and token
        msg = mail.outbox[0]
        self.assertEqual(msg.body, '{} has sent you a new message:\n\n{}'.format(data['nom'], data['message']))

    def test_invalid_form(self):
        data = {'nom': 'Mister Oizo \n Quentin Dupieux',
                'email': 'toto@gmail.com \n toto@gmail.com ',
                'message': 'je ne veux que ton bien'}
        client = Client()
        response = client.post(reverse('core:message'), data, follow=True)
        self.assertEqual(response.status_code, 200)

        # test the error message
        self.assertContains(response, 'Votre message est invalide')
