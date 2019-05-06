from django.db import models

class New_personal(models.Model):
    """
    Модель нового сотрудника
    """
    login = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=20, blank=True)

class Personalarea(models.Model):
    """
    Модель личного кабинета
    """
    login = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    position = models.ManyToManyField(New_personal)

