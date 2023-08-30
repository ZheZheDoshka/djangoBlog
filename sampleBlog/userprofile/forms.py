from django import forms


from userprofile.models import *


class PhotoForm(forms.Form):
    class Meta:
        model = UserProfile
        fields = ('photo', )


class DescriptionForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('description',)