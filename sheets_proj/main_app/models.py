from django.db import models


class SheetData(models.Model):
    number = models.PositiveSmallIntegerField(
        verbose_name='Номер',
    )
    order = models.PositiveIntegerField(
        verbose_name='Номер заказа'
    )
    price_dol = models.DecimalField(
        verbose_name='Цена в $',
        max_digits=12,
        decimal_places=2
    )
    price_rub = models.DecimalField(
        verbose_name='Цена в Руб.',
        max_digits=12,
        decimal_places=2
    )
    shipment_date = models.DateField(
        verbose_name='Дата поставки'
    )

    class Meta:
        verbose_name = 'Данные листа'
        verbose_name_plural = 'Данные листа'
        ordering = ['number']

    def __str__(self):
        return f'Order #{self.order}'
