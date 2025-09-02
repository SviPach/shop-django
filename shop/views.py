from django.shortcuts import render, get_object_or_404
from shop.models import Product, Review


# Create your views here.
def product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product.html', {'product': product})

def index(request):
    products = Product.objects.all()
    reviews = Review.objects.all()
    return render(request, 'index.html', {'products': products, 'reviews': reviews})