from django.conf import settings
from django.db import models
from django.urls import reverse


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True) #variable name, describing the data type of the name which is character field
    slug = models.SlugField(max_length=255, unique=True) #In order to get into a category e.g jumia.com/electronics/...; slugfield describes what should be in this field and it should'nt include special characters; unique=true there should only be one slug with a given name as two categories can't share a name

    class Meta:
        verbose_name_plural = 'categories' #more instructions provided to django about our model, setting the plural name for categories by default django sets it as categorys
    
    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])
    
    def _str_(self):
        return self.name #returning data from the above database by setting default name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE) #To link the product to the category table above to automatically inlcude data in the product
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_creator') #Building a connection to the usertable which django builds automatically and recording the prdouct creator
    title = models.CharField(max_length=255) 
    brand = models.CharField(max_length=255, default='admin') 
    description = models.TextField(blank=True) #text field allows more text than a character field
    image = models.ImageField(upload_to='images/', default='images/default.png') 
    slug = models.SlugField(max_length=255)  
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True) #true or false field
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True) #autonowadd triggered once when product is created 
    updated = models.DateTimeField(auto_now=True) #autonow triggered everytime an update is made
    objects = models.Manager()
    products = ProductManager()
    

    class Meta:
        ordering = ('-created',) #-created orders the data in descending order 

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])
    
    def _str_(self):
        return self.title #returns the default string of the title

