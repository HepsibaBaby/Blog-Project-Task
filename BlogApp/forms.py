from django import forms
from django.contrib.auth.forms import UserCreationForm

from BlogApp.models import Login, Profile


class LoginForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username','password1','password2')

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'



