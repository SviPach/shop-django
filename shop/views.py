from django.shortcuts import render, get_object_or_404
from shop.models import Product, Review, Category


# Create your views here.
def product(request, slug_category, slug_product):
    product = get_object_or_404(
        Product,
        slug=slug_product,
        category__slug=slug_category
    )
    reviews = Review.objects.filter(product=product)
    return render(request, 'product.html', {'product': product, 'reviews': reviews})

def index(request):
    products = Product.objects.all()
    reviews = Review.objects.all()
    return render(request, 'index.html', {'products': products, 'reviews': reviews})

def category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'products': products})