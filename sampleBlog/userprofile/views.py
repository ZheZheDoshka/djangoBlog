from django.shortcuts import render, redirect, get_object_or_404

from django.views import View

from userprofile.models import *
# Create your views here.


class UserProfileView(View):
    template_name = "userprofile/userprofile.html"

    def get(self, request, profile_name):
        profile = get_object_or_404(UserProfile, profile_name=profile_name)
        context = {'profile': profile}
        return render(request, self.template_name, context)

    def post(self, request):
        pass