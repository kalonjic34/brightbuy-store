class Cart():
    
    
    def __init__(self, request):
        self.session = request.session
        
        # returning user - obtain his/her existing session
        cart = self.session.get('session-key')
        
        
        # new users - generate a new session
        if 'session-key' not in request.session:
            cart = self.session['session-key'] = {}
            
        self.cart = cart
        
    def add(self, product, product_qty):
        product_id = str(product.id)
        
        if product_id in self.cart:
            self.cart[product_id]['qty']= product_qty
        else:
            self.cart[product_id] ={'price':str(product.price), 'qty':product_qty}
        self.session.modified = True