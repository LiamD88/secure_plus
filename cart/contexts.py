from django.shortcuts import get_object_or_404
from services1.models import Package

def cart_contents(request):
    """This will allow cart contents to be available when rendering any page on the site"""

    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for item_id, quantity in cart.items():
        package = get_object_or_404(Package, pk=item_id)
        total += quantity * package.price
        cart_items.append({'item_id': item_id, 'quantity': quantity, 'package': package})

    context = {
        'cart_items': cart_items,
        'total': total, 
    }


    return context   

