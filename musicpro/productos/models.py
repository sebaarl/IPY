from django.db import models
from django.db.models.fields import CharField
from django.db.models.deletion import CASCADE
from django.utils.translation import activate
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.shortcuts import reverse

class Categoria(models.Model):
    nombre = models.CharField(max_length=80, null=False)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=80, null=False)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank=False)
    marca = models.ForeignKey(Marca, on_delete = CASCADE)
    imagen = models.ImageField(upload_to='product_images', null=True)
    slug = models.SlugField(unique=True)
    codigo = models.CharField(max_length=20, null=False)
    serie_producto = CharField(max_length=20, null=False)
    precio = models.IntegerField()
    descripcion = models.TextField()
    activate = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

    def get_price(self):
        return "{:.2f}".format(self.precio /100)

    @property
    def in_stock(self):
        return self.stock > 0

    def get_absolute_url(self):
        return reverse("cart:product-detail", kwargs={'slug': self.slug})

def pre_save_product_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(pre_save_product_receiver, sender=Producto)