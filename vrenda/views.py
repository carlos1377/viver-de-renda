# from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import auth
from vrenda import forms
from django.contrib.auth.decorators import login_required
from vrenda.forms import EntradaForm
from django.urls import reverse

from vrenda.models import Entrada, Flow  # type: ignore
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
    form_action = reverse('vrenda:despesas')

    if request.method == 'POST':
        form = forms.EntradaForm(request.POST, instance=Entrada())
        context = {
            'form': form,
            'form_action': form_action,
        }
        if form.is_valid():
            entrada = form.save(commit=False)
            entrada.user = request.user
            flow_id = int(request.POST['flow'])
            flow = Flow.objects.get(id=int(flow_id))
            entrada.flow = flow
            entrada.save()
            return redirect('vrenda:listar_despesas')

        return render(
            request,
            'vrenda/despesas.html',
            context,
        )

    context = {
        'form': EntradaForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'vrenda/despesas.html',
        context
    )


@login_required(login_url='vrenda:login')
def listar_despesas(request):
    despesas = Entrada.objects.filter(user=request.user,).order_by('-date')
    context = {
        'despesas': despesas
    }
    return render(
        request,
        'vrenda/listar_despesas.html',
        context
    )


@login_required(login_url='vrenda:login')
def configuracoes(request):
    context = {}
    return render(
        request,
        'vrenda/configuracoes.html',
        context
    )
