from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from .models import Category, FoodItem, Order, OrderItem, Delivery, CateringRequest 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

 
 
# Create your views here.
def homepage(request):
    return render(request, 'Food/homepage.html') 

def menu(request):
    categories = Category.objects.all()
    food_items = FoodItem.objects.all()
    return render(request, 'Food/menu.html', {'categories': categories, 'food_items': food_items})

# View for displaying details of a specific food item
def food_detail(request, id):
    food_item = get_object_or_404(FoodItem, id=id)
    return render(request, 'food_detail.html', {'food_item': food_item})


def create_order(request):
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

        # Add items to the order
        for key, value in request.POST.items():
            if key.startswith('item_') and value.isdigit():
                food_item_id = key.split('_')[1]
                food_item = FoodItem.objects.get(id=food_item_id)
                OrderItem.objects.create(order=order, food_item=food_item, quantity=int(value))

        return redirect('order_summary', order_id=order.id)
    

    # Render form for creating an order
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
            delivery_status='pending'  # Default status
        )
        return redirect('order_summary', order_id=order.id)  # Redirect to order details or another relevant page

    return render(request, 'Food/create_delivery.html', {'order': order})


def order_summary(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'Food/order_summary.html', {'order': order})


def catering_request(request):
    if request.method == 'POST':
        # Gather data from the form and create a CateringRequest
        CateringRequest.objects.create(
            customer_name=request.POST['customer_name'],
            customer_phone=request.POST['customer_phone'],
            event_date=request.POST['event_date'],
            number_of_guests=request.POST['number_of_guests'],
            menu_preferences=request.POST.get('menu_preferences', ''),
        )
        return redirect('catering_success')

    return render(request, 'Food/catering_request.html')
