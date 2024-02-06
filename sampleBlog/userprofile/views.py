from django.shortcuts import render, redirect, get_object_or_404

from django.views import View

from django.core.files.storage import FileSystemStorage

from userprofile.models import *
from userprofile.forms import *

# Views for userprofile app


class UserProfileView(View):
    """
    View for userprofile page that consists of user profile
    """
    template_name = "userprofile/userprofile.html"
    def get(self, request, profile_name):
        profile = get_object_or_404(UserProfile, profile_name=profile_name)
        photo_form = PhotoForm()
        description_form = DescriptionForm()
        context = {'profile': profile, 'photo_form': photo_form, 'description_form': description_form}
        return render(request, self.template_name, context)

    def post(self, request, profile_name):
        profile = get_object_or_404(UserProfile, profile_name=profile_name)
        if "photo-submit" in request.POST:
            # TD: decouple file uploading
            image = request.FILES['photo']
            fss = FileSystemStorage()
            image = fss.url(fss.save(image.name, image))
            profile.update_photo(image)
        if "description-submit" in request.POST:
            description = request.POST['description']
            profile.update_description(description)
        return redirect(u'/profile/%s' % profile_name)
