from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect
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


def about(request):
    return render(request, 'about.html')


def privacy(request):
    return render(request, 'privacy.html')


def terms(request):
    return render(request, 'terms.html')

def pricing(request):
    return render(request, 'pricing.html')

def account(request):
    if request.user.is_authenticated:
        return render(request, 'account/account_overview.html')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('account')
        else:
            form = AuthenticationForm()

        return render(request, 'account/account_overview.html', {'form': form})
