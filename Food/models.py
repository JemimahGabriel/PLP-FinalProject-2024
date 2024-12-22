from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Category(models.Model):
    name = name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='food_items')
    image = models.ImageField(upload_to='food_images/', blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"Order for {self.customer_name}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    FoodItem = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.FoodItem.name}"

    
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to Django's built-in User model
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

    
    
class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=255)
    delivery_type = models.CharField(max_length=50, choices=[('pickup', 'Pickup'), ('delivery', 'Delivery')])
    delivery_status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('dispatched', 'Dispatched'), ('delivered', 'Delivered')])

    def __str__(self):
        return f"Delivery for Order {self.order.id}"