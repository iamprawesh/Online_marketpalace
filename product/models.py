from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField('Category Name',max_length=50)
    class_name = models.CharField(max_length=50,blank=True,null=True)
    slug = models.SlugField(blank=True, null=True)
    
    def save(self,*args,**kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Category,self).save(*args,**kwargs)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=30)    
    def __str__(self):
        return self.name

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)


    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class Product(models.Model):
    CONDITION_TYPE = (
            ("New","New"),
            ("Used","Used")
        )
    DELIVERY_TYPE = (
            ('Yes','Yes'),
            ('No','No')
        )
    DELIVERY_AREA = (
            ('With in City','With in City'),
            ('AnyWhere in Nepal','AnyWhere in Nepal')
        )
    category  = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)  
    title = models.CharField('Product Title',max_length=100)
    description = models.TextField(max_length=100)
    price = models.IntegerField()
    condition = models.CharField(max_length=100,choices=CONDITION_TYPE)
    image = models.ImageField(upload_to='main_product' )
    # image = models.ImageField(upload_to='category/')
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    home_delivery = models.CharField(max_length=100,choices=DELIVERY_TYPE)
    delivery_area = models.CharField(max_length=100, choices=DELIVERY_AREA,blank=True,null=True)
    home_delivery_price = models.DecimalField(max_digits=4,decimal_places=0,null=True,blank=True)
    price_negotiable = models.CharField(max_length=100,choices=DELIVERY_TYPE)
    featured_post = models.BooleanField(default=False,null=True,blank=True)
    created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True,null=True) 
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)


    def save(self,*args,**kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title[0:20]+'-'+ str(self.id))
        super(Product,self).save(*args,**kwargs)
    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/',blank=True,null=True)

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return self.product.title


