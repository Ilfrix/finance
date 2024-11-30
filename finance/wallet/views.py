from django.shortcuts import render, get_object_or_404, redirect
from wallet.models import Wallet
from .forms import WalletForm

def money(request, pk=0):
    template = 'wallet/money.html'
    wallet = get_object_or_404(
        Wallet,
        pk=pk
    )
    context = {
        'wallet': wallet,
        'wallet_id': pk
    }

    return render(request, template, context)

def update_info(request, pk=0):
    template = 'wallet/money.html'
    instance = get_object_or_404(Wallet, pk=pk)
    form = WalletForm(request.POST or None, instance=instance)
    context = {'form': form,
               'wallet_id': pk}

    if form.is_valid():
        form.save()
        cash = form.cleaned_data['cash']
        card = form.cleaned_data['card']
        deposit = form.cleaned_data['deposit']


        context.update({
            'cash': cash,
            'card': card,
            'deposit': deposit
        })
    return render(request, template, context)