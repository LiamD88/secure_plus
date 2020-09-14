from django.shortcuts import render, redirect, reverse
from django.contrib import messages

def view_cart(request):
    """ Render the main cart page """
    return render(request, 'cart.html')


def add_to_cart(request, id):
    """ Add items to your cart"""
    if request.user.is_authenticated:

        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})

        if id in cart:
            cart[id] += quantity
        else :
            cart[id] = quantity
        
        request.session['cart'] = cart
        messages.success(request, 'You have added one package to your cart!')
    else:
        messages.error(request, 'You must be logged in to add a package to the cart.')
    return redirect(reverse('services1'))


def amend_cart(request, id):

    """ Ability to increase/decrease number of items in cart """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('cart'))

        