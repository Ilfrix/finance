from django.shortcuts import render
from spending.models import Spend
from .forms import SpendForm

def all_spending(request):
    template = 'spending/spendings.html'
    spendings = Spend.objects.filter(user_id=request.user.id)
    context = {
        'spendings': spendings,
    }

    return render(request, template, context)

def update_info(request):
    template = 'spending/spendings.html'
    instance = Spend.objects.filter(user_id=request.user.id)[0]
    form = SpendForm(request.POST or None, instance=instance)
    context = {'form': form,
               'wallet_id': request.user.id}

    if form.is_valid():
        form.save()
        money = form.cleaned_data['money']
        category = form.cleaned_data['category']

        context.update({
            'money': money,
            'category': category
        })
    return render(request, template, context)