from django.shortcuts import render, redirect
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from vrenda import forms
from django.contrib.auth.decorators import login_required
from vrenda.forms import EntradaForm
# Create your views here.


def index(request):
    return render(
        request,
        'vrenda/index.html',
    )


def login_view(request):
    form = forms.CustomAuthenticationForm(request)

    if request.method == 'POST':
        form = forms.CustomAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('vrenda:index')

    return render(
        request,
        'vrenda/login.html',
        {
            'form': form,
        }
    )


@login_required(login_url='vrenda:login')
def logout(request):
    auth.logout(request)
    return redirect('vrenda:index')


@login_required(login_url='vrenda:login')
def despesas(request):
    form = EntradaForm()
    return render(
        request,
        'vrenda/despesas.html',
        context={'form': form}
    )
