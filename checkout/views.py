from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import OrderForm
from django. conf import settings
from .models import OrderLineItem
from services1.models import Package
from django.contrib.auth.decorators import login_required
import stripe

stripe.api_key = settings.STRIPE_PRIVATE




def checkout(request):

    if request.method == 'POST':
        order_form = OrderForm(request.POST)


        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.save()

            cart = request.session.get('cart', {})
            total = 0

            for item_id, quantity in cart.items():
                package = get_object_or_404(Package, pk=item_id)
                total += quantity * package.price
                order_line_item = OrderLineItem(order=order, package=package, quantity=quantity)
                order_line_item.save()   

                payment_stripe = stripe.PaymentIntent.create(
                    amount=int(total * 100),
                    currency=settings.STRIPE_CURRENCY)

                order_form = OrderForm()

            messages.success(request, 'Your order has been placed')
            return redirect(reverse('services1'))
        
        messages.error(request, 'This order has not been processed')
        return redirect(reverse('services1'))


    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Theres nothing in your bag at the moment")
            return redirect(reverse('services1'))
        
        order_form = OrderForm()
          


   
    context = {
            'order_form': order_form,
            'public_key': settings.STRIPE_PUBLIC
            }
    


    return render(request, 'checkout.html', context)


