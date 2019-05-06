from django.db import models

class Confirmation(models.Model):
    """
    Модель подтверждения
    """
    email = models.EmailField(max_length=50, blank=True, unique=True)
    viber = models.CharField(max_length=50, blank=True, unique=True)
    sms = models.CharField(max_length=50, blank=True)