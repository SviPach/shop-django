"""
URL configuration for my_django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from shop import views as shop_views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', shop_views.index),
                  path('category/<slug:slug_category>/<slug:slug_product>/', shop_views.product),
                  path('category/<slug:category_slug>/', shop_views.category),
                  path('about/', shop_views.about),
                  path('privacy/', shop_views.privacy),
                  path('terms/', shop_views.terms),
                  path('pricing/', shop_views.pricing),
                  path('account/', shop_views.account, name='account'),
                  path('account/cart/', shop_views.cart_detail, name='cart'),
                  path('account/cart/add/<int:product_id>', shop_views.add_to_cart, name='add_to_cart'),
                  path('cart/clear/', shop_views.cart_clear, name='cart_clear'),
                  path('account/', include('django.contrib.auth.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
