from django.db import models

# Create your models here.
from django.urls import reverse



class Shaurma_Food(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    composition = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    price = models.IntegerField(default=True)
    sizes = models.TextField(default='')
    sauces = models.TextField(default='')
    cat = models.ForeignKey('Category',on_delete=models.PROTECT,null=True)

    def get_absolute_url(self):
        return reverse('product', kwargs={'shaurma_slug': self.slug})

    class Meta:
        pass


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
