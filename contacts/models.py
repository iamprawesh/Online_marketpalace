from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator
# Create your models here.
class Contact(models.Model):
	phone_regex = RegexValidator(regex=r'^\d{8,10}$', message="Phone number must be entered in the upto 10 digits")
	product_title = models.CharField(max_length=200)
	listing_id = models.IntegerField()
	listing_slug = models.SlugField()
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phone = models.CharField(validators=[phone_regex], max_length=10, blank=True) # validators should be a list
	message = models.TextField(max_length=100,blank=True)
	contact_date = models.DateTimeField(default=datetime.now,blank=True)
	user_id = models.IntegerField(blank=True)

	def __str__(self):
		return self.name		
