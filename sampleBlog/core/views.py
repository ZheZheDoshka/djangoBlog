from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views import View

from core.forms import RegistrationForm, LoginForm


def index(request):
    return render(request, 'core/index.html')


class Registration(View):
    template_name = 'authentication/registration.html'

    def get(self, request):
        form = RegistrationForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        pass


class Login(View):
    template_name = 'authentication/login.html'

    def get(self, request):
        form = LoginForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        pass


def logout_view(request):
    logout(request)


'''def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...'''