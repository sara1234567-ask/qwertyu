from django.db import models

class IceCream(models.Model):
    name = models.CharField(max_length=50)
    flavor = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.flavor})"

class Kiosk(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    ice_creams = models.ManyToManyField(IceCream, related_name='kiosks')

    def __str__(self):
        return self.name

class Parent(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Child(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return self.name
