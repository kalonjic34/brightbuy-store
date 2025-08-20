class cart():
    
    
    def __init__(self, request):
        self.session = request.session
        
        # returning user - obtain his/her existing session
        cart = self.session.get('session-key')
        
        
        # new users - generate a new session
        if 'session-key' not in request.session:
            cart = self.session['session-key'] = {}
            
        self.cart = cart