from django.shortcuts import render
from wallet.models import Wallet
from .forms import WalletForm

def money(request):
    template = 'wallet/money.html'
    user_id = request.user.id
    wallet = None
    try:
        wallet = Wallet.objects.filter(user_id=user_id)[0]
    except Exception:
        pass

    context = {
        'wallet': wallet,
        'wallet_id': request.user.id
    }

    return render(request, template, context)

def update_info(request):
    template = 'wallet/money.html'
    instance = Wallet.objects.filter(user_id=request.user.id)[0]
    form = WalletForm(request.POST or None, instance=instance)
    context = {'form': form,
               'wallet_id': request.user.id}

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
