from django.db import models

# Create your models here.
class Person(models.Model):
    first = models.TextField()
    last  = models.TextField()

    def __repr__(self) -> str:
        return self.first


class Products(models.Model):
    name    = models.TextField()
    company = models.TextField()
    color = models.TextField()
    ram = models.TextField()
    memory = models.TextField()
    price = models.FloatField()
    img_url = models.TextField()

    def __repr__(self) -> str:
        return self.name