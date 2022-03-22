from django.forms import ModelForm

from .models import Order, Product


class OrderForm(ModelForm):
    class Meta :
        model = Order
        fields = ['product','status','note']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field, in self.fields.items():
            field.widget.attrs.update({'class' : 'form-control'})



class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field, in self.fields.items():
            field.widget.attrs.update({'class' : 'form-control'})
