from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    slug=models.SlugField(unique=True,max_length=20)
    cover = models.ImageField(upload_to="/")

    def get_absolute_url(self):
        return reverse('store:get_category',args=[self.slug])
    
    def __str__(self) -> str:
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.PositiveSmallIntegerField()
    slug = models.SlugField(unique=True,max_length=30)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    visible = models.BooleanField(default=False)
    quantity = models.PositiveSmallIntegerField()

    # images


    def get_absolute_url(self):
        return reverse("store:get_product",args=[self.slug])
    
    def __str__(self) -> str:
        return "Product:"+self.name+"\tPrice:"+str(self.price)