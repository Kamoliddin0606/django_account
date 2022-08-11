from http.client import IM_USED
from pyexpat import model
from django import forms
from django.contrib.auth.models import User

class Editprofile(forms.ModelForm):
    class Meta:
        model =User
        fields= ['email', 'last_name', 'first_name']    
