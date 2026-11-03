from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def index(request):
    products = Product.objects.all()
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(name__icontains=search_query)
    return render(request, 'index.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def add_to_cart(request, product_id):
    if 'cart' not in request.session:
        request.session['cart'] = {}
    
    cart = request.session['cart']
    product_id_str = str(product_id)
    
    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1
        
    request.session.modified = True
    return redirect('cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * quantity
        total_price += subtotal
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })
        
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
def checkout(request):
    # Clear the cart from the session after purchase
    if 'cart' in request.session:
        del request.session['cart']
    return render(request, 'order_success.html')    