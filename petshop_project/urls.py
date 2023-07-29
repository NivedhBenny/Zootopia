"""
URL configuration for petshop_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from zootopia import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # new


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.index,name='index pet'),
    path('add_pets',views.add_pets,name='add_pets'),
    path('add_products',views.add_products,name='add_products'),
    path('view_pets',views.view_pets,name='view_pets'),
    path('view_products',views.view_products,name='view_products'),
    path('delete_pet/<int:id>',views.delete_pet,name='delete_pet'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('edit_pet/<int:id>',views.edit_pet,name='edit_pet'),
    path('register_page',views.register_page,name='register_page'),
    path('login_page',views.login_page,name='login_page'),
    path('userregister',views.userregister,name='userregister'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('show_pets',views.show_pets,name='show_pets'),
    path('show_products',views.show_products,name='show_products'),
    path('addpets_page',views.addpets_page,name='addpets_page'),
    path('addproducts_page',views.addproducts_page,name='addproducts_page'),
    path('logout',views.logout,name='logout'),
    path('search_pet',views.search_pet,name='search_pet'),
    path('search_product',views.search_product,name='search_product'),
    path('owner_page',views.owner_page,name='owner_page'),
    path('customer_page',views.customer_page,name='customer_page'),
    path('address_page',views.address_page,name='address_page'),
    path('pay_page',views.pay_page,name='pay_page'),
    path('payment_page',views.payment_page,name='payment_page'),
    path('cart_page',views.cart_page,name='cart_page'),
    path('otp_page',views.otp_page,name='otp_page'),
    path('thankyou_page',views.thankyou_page,name='thankyou_page'),
    path('add_to_cart_pet/<int:id>',views.add_to_cart_pet,name='add_to_cart_pet'),
    path('add_to_cart_product/<int:id>',views.add_to_cart_product,name='add_to_cart_product'),
    path('order_pay',views.order_pay,name='order_pay'),
    path('payment',views.payment,name='payment'),
]

urlpatterns += staticfiles_urlpatterns() # new

if settings.DEBUG:
    urlpatterns+=(static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT))
    