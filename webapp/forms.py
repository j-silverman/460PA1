from django import forms
from webapp.models import people

class SubmitPerson(forms.Form):
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    email = forms.CharField(max_length = 30)
    home_town = forms.CharField(max_length= 20)
    gender = forms.CharField(max_length=1)
    password = forms.CharField(max_length = 20)
    date_of_birth = forms.DateField()
        