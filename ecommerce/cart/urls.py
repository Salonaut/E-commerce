from django.urls import path
from .views import CartModalView, AddToCartView


app_name = 'cart'
urlpatterns = [
    path('', CartModalView.as_view(), name='cart_modal'),
    path('add/<slug:slug>', AddToCartView.as_view(), name='add_to_cart'),

]