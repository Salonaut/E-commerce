from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.generic import View
from .forms import OrderForm
from .models import OrderItem, Order
from cart.views import CartMixin
from cart.models import Cart
from main.models import ProductSize
from django.shortcuts import get_object_or_404
from decimal import Decimal
from payment.views import create_stripe_checkout_session



@method_decorator(login_required(login_url='/users/login'), name='dispatch')
class CheckoutView(CartMixin, View):
    def get(self, request):
        cart = self.get_cart(request)

        if cart.total_items == 0:
            if request.headers.get('HX-Request'):
                return TemplateResponse(request, 'orders/empty_cart.html', {'message': 'Your cart is empty.'})
            return redirect('cart:cart_modal')


        total_price = cart.subtotal

        form = OrderForm(user=request.user)
        context = {
            'form': form,
            'cart': cart,
            'cart_items': cart.items.select_related(
                'product',
                'product_size__size'
            ).order_by('-added_at'),
            'total_price': total_price
        }

        if request.headers.get('HX-Request'):
            return TemplateResponse(request, 'orders/checkout_content.html', context)

        return render(request, 'orders/checkout.html', context)
