from django.db import models
# users/models.py
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Customer(models.Model):
    Cname = models.CharField(max_length=255)
    Cnumber = models.CharField(max_length=255)
    Cemail = models.CharField(max_length=255)

    def __str__(self):
        return self.Cname
