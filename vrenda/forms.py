from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))

    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'type': 'hidden',
        }
    ))

    class Meta:
        model = User
        fields = ('email', 'password', 'username')

    field_order = ('email', 'password', 'username')
