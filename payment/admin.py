from django.contrib import admin

from .models import Checkout, Orderitem

admin.site.register(Checkout)
admin.site.register(Orderitem)