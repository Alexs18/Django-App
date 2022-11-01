from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Login(TemplateView):
    template_name: str = 'login/login.html'

class Logout(TemplateView):
    template_name: str = 'login/logout.html'