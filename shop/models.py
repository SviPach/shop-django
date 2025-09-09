from django.db import models
from django.db.models import Avg
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()
    summary = models.CharField(max_length=300)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    @property
    def average_rating(self):
        result = self.reviews.aggregate(avg_rating=Avg('rating'))
        return result['avg_rating'] or 0

    @property
    def average_rating_gold(self):
        return range(round(self.average_rating))

    @property
    def average_rating_gray(self):
        return range(5 - round(self.average_rating))

    @property
    def amount_of_ratings(self):
        return self.reviews.count()


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def stars_gold(self):
        return range(self.rating)

    @property
    def stars_gray(self):
        return range(5 - self.rating)


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='images', default='empty.png')

    def __str__(self):
        filename = self.image.url.split('/')[-1]
        return f"{self.product.name} - {filename}"

    class Meta:
        ordering = ['product__name']


class Cart(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cart"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())

    def add_product(self, product, quantity=1):
        """Add a product"""
        item, created = CartItem.objects.get_or_create(cart=self, product=product)
        if not created:
            item.quantity += quantity
        else:
            item.quantity = quantity
        item.save()
        return item

    def clear(self):
        """Clear the cart"""
        self.items.all().delete()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("cart", "product")

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    def total_price(self):
        return self.product.price * self.quantity


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_cart_for_user(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)
