from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=254,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(render_value = True, attrs={'class': 'form-control', 'placeholder': 'Your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(render_value = True, attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
