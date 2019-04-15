from core.views import AccueilView, ContactView
from django.urls import path


app_name = 'core'

urlpatterns = [
    path('', AccueilView.as_view(), name='home'),
    path('message/submit', ContactView.as_view(), name='message')
]

