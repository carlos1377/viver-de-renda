from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from vrenda.models import Entrada  # type: ignore
from vrenda.models import Flow  # type: ignore


class CustomAuthenticationForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))

    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'password',)

    field_order = ('username', 'password',)


class EntradaForm(forms.ModelForm):

    value = forms.DecimalField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'type': 'number',
        }
    ))
    observation = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
        }
    ))

    flow = forms.ModelChoiceField(
        queryset=Flow.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
            }
        ))

    class Meta:
        model = Entrada
        fields = ('value', 'flow', 'observation')

# class ConfigurationForm(forms.ModelForm):
