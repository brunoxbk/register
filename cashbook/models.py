from django.db import models
from datetime import date


class Movement(models.Model):
    class TypesChoices(models.TextChoices):
        INCOME = 'REVENUE', "Receita"
        EXPENSE = 'EXPENSE', "Despesa"

    user = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE,
        null=True, blank=True, related_name='user_moves')
    close = models.BooleanField("Recebida", default=False)
    kind = models.CharField('Natureza', max_length=10,
                            choices=TypesChoices.choices)
    date = models.DateField('Data', null=True, blank=True)
    description = models.TextField("Texto", null=True, blank=True)
    received_date = models.DateField('Data Recebiento', null=True, blank=True)
    value = models.DecimalField(
        "Valor", decimal_places=2, max_digits=8,
        null=False, blank=False, default=0)

    @property
    def is_past_due(self):
        return date.today() > self.date and self.close

    class Meta:
        verbose_name = "Movimento"
        verbose_name_plural = "Movimentação"

    def __str__(self):
        return self.description
