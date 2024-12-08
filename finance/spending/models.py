from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Слаг')
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='Порядок отображения'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
  
    def __str__(self):
        return self.title


class Spend(models.Model):
    money = models.DecimalField(
        max_digits=9, 
        decimal_places=2, 
        verbose_name='Сумма'
    )
    
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='spendings',
        verbose_name='Категория',
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = 'Трата'
        verbose_name_plural = 'Траты'

    def __str__(self):
        return str(self.money)
