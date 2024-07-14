from django.contrib import admin
from .models import User, Product, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'image']
    ordering = ['name', '-price']
    list_filter = ['name', 'description']


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'password', 'age']
    ordering = ['email', '-age']
    list_filter = ['name', 'age']



class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date_ordered', 'total_price']


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

