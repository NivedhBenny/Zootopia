from django.contrib import admin
from .models import Pets
from .models import Products,Register_User,Cart,Pay,Address,Order

admin.site.register(Pets)
admin.site.register(Products)
admin.site.register(Register_User)
admin.site.register(Cart)
admin.site.register(Pay)
admin.site.register(Address)
admin.site.register(Order)