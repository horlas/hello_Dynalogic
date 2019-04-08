from core.views import AccueilView
from django.urls import path


app_name = 'core'

urlpatterns = [
    path('', AccueilView.as_view(), name='accueil'),
]