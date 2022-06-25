
class Cart():
    def __init__(self, request):
        if request.session.get('cart') is not None:
            request.session['cart'] = {}

        self.cart = request.session['cart']
        self.session = request.session
    
    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[str(product.id)] = {
                'quantity': 0,
                'price': str(product.price),
            }

        if override_quantity:
            self.cart[product.id]['quantity'] = quantity
        else:
            self.cart[product.id]['quantity'] += quantity

        self.session.modified = True

    def remove(self, product): 
        del self.cart[str(product.id)] 
        
        self.session.modified = True