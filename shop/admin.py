from django.contrib import admin
from shop.models import Product, Review, Category, ProductImage

# Register your models here.
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(ProductImage)
