from django.shortcuts import render, get_object_or_404, redirect
from spending.models import Spend
# from .forms import SpendForm

def all_spending(request):
    template = 'spending/spendings.html'
    spendings = Spend.objects.all()
    context = {
        'spendings': spendings,
    }
    print(context)

    return render(request, template, context)