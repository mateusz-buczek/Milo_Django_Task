from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
        ]


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'birth_date',
            'random_number',
        ]
