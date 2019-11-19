from django.contrib import admin
from .models import Category,Product,ProductImage,State,City
# Register your models here.
admin.site.register(Category)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Product)
admin.site.register(ProductImage)

