from django import forms
from .models import Spend


class SpendForm(forms.ModelForm):
    class Meta:
        model = Spend
        fields = (
            'money', 'category'
        )

    def clean(self):
        super().clean()
        money = self.cleaned_data['money']
        category_id = self.cleaned_data['category']
        # user_id = self.cleaned_data['user_id']
