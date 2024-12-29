from django.contrib.auth.models import User
from Food.models import Category, FoodItem, Order, OrderItem, Customer, Delivery, CateringRequest

# Create sample categories
categories = [
    {"name": "Appetizers", "description": "Starters for your meals."},
    {"name": "Main Course", "description": "Delicious main dishes."},
    {"name": "Desserts", "description": "Sweet treats for all."},
]
for cat in categories:
    Category.objects.create(**cat)

# Create sample food items
food_items = [
    {"name": "Spring Rolls", "description": "Crispy rolls", "price": 5.99, "category_id": 1, "is_available": True},
    {"name": "Chicken Curry", "description": "Spicy curry", "price": 12.50, "category_id": 2, "is_available": True},
    {"name": "Chocolate Cake", "description": "Rich and creamy", "price": 6.75, "category_id": 3, "is_available": True},
]
for item in food_items:
    FoodItem.objects.create(**item)

# Create sample user and customer
user = User.objects.create_user(username="test_user", password="password123")
customer = Customer.objects.create(user=user, name="Sally Flora", email="sally@example.com", phone="08123456789", address="123 Main St")

# Create sample orders
order = Order.objects.create(
    customer_name="Sally Flora",
    customer_phone="08123456789",
    customer_address="123 Main St",
    is_pickup=False,
    status="Pending",
    user=user,
)

# Create order items
order_items = [
    {"order": order, "food_item_id": 1, "quantity": 2},
    {"order": order, "food_item_id": 2, "quantity": 1},
]
for item in order_items:
    OrderItem.objects.create(**item)

# Create sample delivery
Delivery.objects.create(  
    order=order,
    delivery_address="123 Main St",
    delivery_type="delivery",
    delivery_status="pending",
)

# Create sample catering request
CateringRequest.objects.create(
    customer_name="Alice Johnson",
    phone_number="08098765432",
    email="alice@example.com",
    event_date="2024-12-31",
    event_type="wedding",
    guest_count=100,
)
