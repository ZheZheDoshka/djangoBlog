from django.shortcuts import render, redirect, get_object_or_404

from django.views import View

from userprofile.models import *
from userprofile.forms import *
# Create your views here.


class UserProfileView(View):
    template_name = "userprofile/userprofile.html"

    def get(self, request, profile_name):
        profile = get_object_or_404(UserProfile, profile_name=profile_name)
        photo_form = PhotoForm()
        description_form = PhotoForm()
        context = {'profile': profile, 'photo_form': photo_form, 'description_form': description_form}
        return render(request, self.template_name, context)

    def post(self, request, profile_name):
        image = request.POST['photo']
        profile = get_object_or_404(UserProfile, profile_name=profile_name)
        profile.update_photo(image)
        return redirect("/")


