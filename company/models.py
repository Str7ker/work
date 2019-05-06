from django.db import models

class Company(models.Model):
    """
    Модель компании
    """
    name = models.CharField(max_length=50, blank=True)
    inn = models.CharField(max_length=20, blank=True)
    ogrn = models.CharField(max_length=50, blank=True)
    kpp = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=300, blank=True)
    post_address = models.CharField(max_length=300, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    name_director = models.CharField(max_length=50, blank=True)
    post_director = models.CharField(max_length=50, blank=True)

class Position(models.Model):
    """
    Модель должности персонала
    """
    position = models.CharField(max_length=200, help_text="Должность человека", blank=True)

    def __str__(self):
        return self.position

class Personal(models.Model):
    """
    Модель персонала
    """
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    position = models.ManyToManyField(Position, help_text="Должность человека")

class Rating(models.Model):
    """
    Модель рейтинга
    """
    id = models.OneToOneField(Company, on_delete = models.CASCADE, primary_key=True)
    rating = models.BigIntegerField(blank=True)