from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('menu/', views.menu, name='menu'),
    path('food/<int:food_id>/', views.food_detail, name='food_detail'),
    path('order/', views.create_order, name='create_order'),
    path('order/summary/<int:order_id>/', views.order_summary, name='order_summary'),
    path('delivery/create/<int:order_id>/', views.create_delivery, name='create_delivery'),
    path('catering/request/', views.catering_request, name='catering_request'),
    path('login/', auth_views.LoginView.as_view(template_name='Food/login.html'), name='login'),
    
]

