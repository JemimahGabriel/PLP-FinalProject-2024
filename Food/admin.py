from django.contrib import admin
from .models import Category, FoodItem, Order, OrderItem, Delivery, CateringRequest

class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'name', 'category', 'price', 'is_available')  # Add 'id' here


# Register your models here.
admin.site.register(Category)
admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Delivery)
admin.site.register(CateringRequest)


