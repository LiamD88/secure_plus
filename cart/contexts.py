from django.shortcuts import get_object_or_404
from services1.models import Packages

def cart_contents(request):
    """This will allow cart contents to be available when rendering any page on the site"""

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    

    for id, quantity in cart,items():
        package = get_object_or_404(Packages, pk=id)
        total += quantity * package.price
        cart_items.append({'id': id, 'quantity': quantity, 'package': package})

    return ('cart_items': cart_items, 'total': total)    
