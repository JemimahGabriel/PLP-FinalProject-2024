from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from .models import Category, FoodItem, Order, OrderItem, Delivery, CateringRequest 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import CateringRequest
from django.shortcuts import render, redirect


 
 
# Create your views here.
def homepage(request):
    return render(request, 'Food/homepage.html') 

def menu(request):
    categories = Category.objects.all()
    food_items = FoodItem.objects.all()
    return render(request, 'Food/menu.html', {'categories': categories, 'food_items': food_items})

# View for displaying details of a specific food item
def food_detail(request, food_item_id):
    food_item = get_object_or_404(FoodItem, id=food_item_id)
    return render(request, 'Food/food_detail.html', {'food_item': food_item})

@login_required
def create_order(request):
    order = None  # Initialize the order as None to handle the GET request
    if request.method == 'POST':
        # Capture order-level details
        customer_name = request.POST['customer_name']
        customer_phone = request.POST['customer_phone']
        customer_address = request.POST.get('customer_address', None)
        is_pickup = 'pickup' in request.POST

        # Create the order
        order = Order.objects.create(
            customer_name=customer_name,
            customer_phone=customer_phone,
            customer_address=customer_address if not is_pickup else None,
            is_pickup=is_pickup,
            user=request.user
        )

        # Add items to the order based on form data
        for key, value in request.POST.items():
            if key.startswith('item_') and value.isdigit():
                food_item_id = key.split('_')[1]  # Extracting the food_item_id from the field name
                food_item = FoodItem.objects.get(id=food_item_id)
                OrderItem.objects.create(order=order, food_item=food_item, quantity=int(value))
        
        # Redirect to the order summary page after creating the order
        return redirect('order_summary', order_id=order.id)

    # Handle GET request to render the order creation form
    food_items = FoodItem.objects.filter(is_available=True)
    return render(request, 'Food/create_order.html', {'food_items': food_items})



@login_required
def create_delivery(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == 'POST':
        delivery_address = request.POST.get('delivery_address')
        delivery_type = request.POST.get('delivery_type')
        
        # Create the Delivery instance
        delivery = Delivery.objects.create(
            order=order,
            delivery_address=delivery_address,
            delivery_type=delivery_type,
            delivery_status='pending', # Default status
        )
            
        
        # Once delivery is created, mark the order as completed      
         # Save the order with the updated status
                
        return redirect('order_summary', order_id=order.id)  # Redirect to order details or another relevant page

    return render(request, 'Food/create_delivery.html', {'order': order})

def complete_order(request, order_id):
    # Retrieve the order using the order_id
    order = get_object_or_404(Order, id=order_id)

    # Update the order status to 'Completed'
    order.status = 'Completed'
    print(f"Updating order status to: {order.status}")
    order.save()

    # Redirect to the order summary or any other page as needed
    return redirect('order_summary', order_id=order.id)
    

def order_summary(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    # Initialize total price variable
    total_price = 0

    # Fetch order items and calculate the total price for each item
    order_items = order.orderitem_set.all()
    for item in order_items:
        item.total_price = item.food_item.price * item.quantity  # Calculate the price for each item
        total_price += item.total_price  # Add it to the overall total

    # Pass the total price, order, and order items to the template
    return render(request, 'Food/order_summary.html', {
        'order': order,
        'order_items': order_items,
        'total_price': total_price
    })




def catering_request(request):
    if request.method == 'POST':
        # Gather data from the form
        customer_name = request.POST['customer_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        event_date = request.POST['event_date']
        event_type = request.POST['event_type']
        guest_count = int(request.POST['guest_count'])
        special_requests = request.POST.get('special_requests', '')

        # Define event type pricing logic
        if event_type == 'wedding':
            price_per_guest = 50
        elif event_type == 'birthday':
            price_per_guest = 30
        elif event_type == 'corporate':
            price_per_guest = 40
        else:
            price_per_guest = 20  # Default price for "other" or custom events

        # Calculate the total price
        total_price = price_per_guest * guest_count

        # Create the CateringRequest instance (optional, for storing data)
        CateringRequest.objects.create(
            customer_name=customer_name,
            phone_number=phone_number,
            email=email,
            event_date=event_date,
            event_type=event_type,
            guest_count=guest_count,
            special_requests=special_requests
        )

        # Redirect to success page and pass the necessary data to display
        return render(request, 'Food/catering_success.html', {
            'customer_name': customer_name,
            'phone_number': phone_number,
            'email': email,
            'event_date': event_date,
            'event_type': event_type,
            'guest_count': guest_count,
            'special_requests': special_requests,
            'total_price': total_price
        })

    return render(request, 'Food/catering_request.html')
