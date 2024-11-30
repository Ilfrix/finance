from django.shortcuts import render
from wallet.models import Wallet

def index(request):
    template = 'homepage/index.html'
    value = Wallet.objects.all().count()
    context = {'value': value}
    return render(request, template, context)
