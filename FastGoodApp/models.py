from django.db import models

# Create your models here.
class Shaurma_Food(models.Model):
    title = models.CharField(max_length=255)
    composition = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    price = models.IntegerField(default=True)
    sizes = models.TextField(default='')
    sauces = models.TextField(default='')