from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View


from core.forms import RegistrationForm, LoginForm
from core.models import User
from userprofile.models import UserProfile


def index(request):
    return render(request, 'core/index.html')


class Registration(View):
    """View for Registration form."""
    template_name = 'authentication/registration.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/")
        form = RegistrationForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username, email, password)
            user.role = User.UserRole.USER
            user.save()
            UserProfile(user=get_object_or_404(User, username=username), profile_name=username).save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("/")
        else:
            return redirect("/registration/")


class Login(View):
    """View for Login form"""
    template_name = 'authentication/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/")
        form = LoginForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        # form = LoginForm(request.POST)
        # if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        return redirect("/login/")


@login_required(redirect_field_name="/login/")
def logout_view(request):
    """Logout action"""
    logout(request)
    return redirect("/login/")
