from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View


from core.forms import RegistrationForm, LoginForm


def index(request):
    return render(request, 'core/index.html')


class Registration(View):
    template_name = 'authentication/registration.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/")
        form = RegistrationForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        # username = request.POST['username']
        # password = request.POST['password1']
        return redirect("/")


class Login(View):
    template_name = 'authentication/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/")
        form = LoginForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return redirect("/login/")


@login_required(redirect_field_name="/login/")
def logout_view(request):
    logout(request)
    return redirect("/login/")
