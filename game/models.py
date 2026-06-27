from django.db import models

# Create your models here.
class Confederation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)
    continent = models.ForeignKey(
        Confederation,
        on_delete=models.CASCADE,
        related_name="countries"
    )

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    clubs = models.ManyToManyField(Club)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.name