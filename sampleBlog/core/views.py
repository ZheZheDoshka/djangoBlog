from django.shortcuts import render

from core.forms import RegistrationForm


def index(request):
    return render(request, 'core/index.html')


def registration(request):
    form = RegistrationForm()
    context = {'form':form}
    return render(request, 'authentication/registration.html', context)


def login(request):
    form = RegistrationForm()
    context = {'form':form}
    return render(request, 'authentication/login.html', context)