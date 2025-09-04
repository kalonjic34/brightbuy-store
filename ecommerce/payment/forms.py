from django import froms
from . models import ShippingAddress

class ShippingForm(Forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['full_name', 'email', 'address1','address2', 'city','state','zipcode']
        exclude = ['user', ]
        