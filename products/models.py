from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 255, blank = True, null = True)
    price = models.DecimalField(max_digits = 10, decimal_places=2, null = True)

    def __str__(self):
        return "Product: {} | Price: {}".format(self.name, self.price)