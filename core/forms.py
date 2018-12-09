from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(required=True, max_length=50, widget=forms.HiddenInput())#(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'username']

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())#required=True, max_length=50,
                                 #widget=forms.HiddenInput()) ()

    class Meta:
            model = User
            fields = ['email','password']


       