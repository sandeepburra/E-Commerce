from django.db import models
from .helpers import RandomFileName 
# Create your models here.
class Product(models.Model):
    asin = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    product_type_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    price = models.FloatField()
    product_img = models.CharField(max_length=200)
    product_Url = models.CharField(max_length=500)

class Image(models.Model):
    image = models.ImageField(upload_to = RandomFileName('pics'))


