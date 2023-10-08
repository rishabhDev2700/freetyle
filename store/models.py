from django.utils import timezone
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
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
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()
    tags = TaggableManager()
    # images


    def get_absolute_url(self):
        return reverse("store:get_product",args=[self.slug])
    
    def __str__(self) -> str:
        return "Product:"+self.name+"\tPrice:"+str(self.price)
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id: # type: ignore
            self.date_added = timezone.now()
        self.date_updated = timezone.now()
        return super(Product, self).save(*args, **kwargs)

