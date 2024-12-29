from django.test import TestCase
from .models import Category, FoodItem, Order,  OrderItem, Customer, Delivery, CateringRequest
from django.contrib.auth.models import User
 #Create your tests here. 
class PopulateDataTestCase(TestCase):
    
    def setUp(self):
        # Creating test categories
        self.category1 = Category.objects.create(name="Pizza", description="Delicious pizza")
        self.category2 = Category.objects.create(name="Pasta", description="Fresh pasta")
        
        # Creating test food items
        self.food_item1 = FoodItem.objects.create(
            name="Margherita Pizza",
            description="Classic pizza with cheese and tomatoes",
            price=10.99,
            category=self.category1,
            is_available=True
        )
        
        self.food_item2 = FoodItem.objects.create(
            name="Spaghetti Bolognese",
            description="Classic Italian pasta",
            price=8.99,
            category=self.category2,
            is_available=True
        )
        
        # Creating test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Creating test customer
        self.customer = Customer.objects.create(
            user=self.user, name="Test Customer", email="test@example.com",
            phone="1234567890", address="Test Address"
        )
        
        # Creating test order
        self.order = Order.objects.create(
            customer_name="Test Order", customer_phone="0987654321", 
            customer_address="Test Address", user=self.user, is_pickup=True
        )
        # Adding items to order
        self.order_item = OrderItem.objects.create(
            order=self.order, food_item=self.food_item1, quantity=2
        )
        
        # Creating a test catering request
        self.catering_request = CateringRequest.objects.create(
            customer_name="John Doe", phone_number="1234567890",
            email="john@example.com", event_date="2024-12-25", 
            event_type="wedding", guest_count=100
        )

    def test_category_creation(self):
        """Test if categories are created correctly."""
        self.assertEqual(self.category1.name, "Pizza")
        self.assertEqual(self.category2.name, "Pasta")

    def test_food_item_creation(self):
        """Test if food items are created correctly."""
        self.assertEqual(self.food_item1.name, "Margherita Pizza")
        self.assertEqual(self.food_item2.name, "Spaghetti Bolognese")

    def test_order_creation(self):
        """Test if order and order items are created correctly."""
        self.assertEqual(self.order.customer_name, "Test Order")
        self.assertEqual(self.order_item.food_item.name, "Margherita Pizza")

    def test_catering_request_creation(self):
        """Test if catering request is created correctly."""
        self.assertEqual(self.catering_request.customer_name, "John Doe")
        self.assertEqual(self.catering_request.event_type, "wedding")
        self.assertEqual(self.catering_request.total_cost, 5000)  # Assuming 50 per guest for weddings

