from core.views import AccueilView, ContactView
from django.urls import path


app_name = 'core'

urlpatterns = [
    path('', AccueilView.as_view(), name='home'),
    path('massage/submit', ContactView.as_view(), name='message')
]