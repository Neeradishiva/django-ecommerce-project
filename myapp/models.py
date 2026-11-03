from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.IntegerField()
    image=models.ImageField(upload_to='products/',null=True,blank=True)

    def _str_(self):
        return self.name
