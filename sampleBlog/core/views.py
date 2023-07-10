from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View


from core.forms import RegistrationForm, LoginForm
from core.models import User


def index(request):
    return render(request, 'core/index.html')


class Registration(View):
    """Registration form"""
    template_name = 'authentication/registration.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/")
        form = RegistrationForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password1']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password)
        user.role = User.UserRole.USER
        user.save()
        return redirect("/")


class Login(View):
    """Login form"""
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
    """Logout action"""
    logout(request)
    return redirect("/login/")
