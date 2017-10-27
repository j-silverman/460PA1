from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from webapp.models import Photos

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    email = forms.CharField(max_length = 30)
    home_town = forms.CharField(max_length= 20)
    gender = forms.CharField(max_length=1)
    date_of_birth = forms.DateField()

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email','home_town','gender','date_of_birth','password1','password2')

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ('caption','photo_data')
