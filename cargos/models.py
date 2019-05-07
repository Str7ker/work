from django.db import models
from django.utils.translation import gettext as _


class Cargos(models.Model):
    """
    Модель грузов
    """
    type = models.CharField(_('Тип груза '), max_length=30, blank=True)
    at = models.CharField(_('Вес груза '), max_length=10, blank=True)
    volume = models.CharField(_('Объем груза '), max_length=10, blank=True)

    class Meta:
        verbose_name = 'Груз'
        verbose_name_plural = 'Грузы'
