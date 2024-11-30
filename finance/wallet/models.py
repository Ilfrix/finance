from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Wallet(models.Model):
    cash = models.DecimalField(
        max_digits=9, 
        decimal_places=2, 
        verbose_name='Наличные'
    )
    card = models.DecimalField(
        max_digits=9, 
        decimal_places=2,
        verbose_name='Карта'
    )
    deposit = models.DecimalField(
        max_digits=9, 
        decimal_places=2,
        verbose_name='Депозит'
    )

    class Meta:
        verbose_name = 'Кошелек'
        verbose_name_plural = 'Кошельки'

    def __str__(self):
        return str(self.cash)
