from django import forms
from .models import Wallet


class WalletForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = (
            'cash', 'card', 'deposit',
        )

    def clean(self):
        super().clean()
        cash = self.cleaned_data['cash']
        card = self.cleaned_data['card']
        deposit = self.cleaned_data['deposit']
