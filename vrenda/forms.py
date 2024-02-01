from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from vrenda.models import Entrada
from vrenda.models import Flow


class CustomAuthenticationForm(AuthenticationForm):
    # email = forms.EmailField(required=False, widget=forms.EmailInput(
    #     attrs={
    #         'class': 'form-control',
    #     }
    # ))
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
        }
    ))
    observation = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
        }
    ))

    flow = forms.ChoiceField(widget=forms.Select(
        attrs={
            'class': 'form-select',
        }
    ))

    class Meta:
        model = Entrada
        fields = ('value', 'flow', 'observation')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['flow'].choices = [
            (flow.id, flow.name) for flow in Flow.objects.all()]
