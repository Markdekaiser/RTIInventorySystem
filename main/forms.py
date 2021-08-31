from django import forms
from django.contrib.admin import widgets
from .models import Requesition, Product, Customer

class RequestForm(forms.ModelForm):
    class Meta:
        model = Requesition
        fields = '__all__'
        exclude = [
            'status','requested_by'
        ]

    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        for fname,f in self.fields.items():
            f.widget.attrs['class'] = 'form-control input-lg'
            f.widget.attrs['aria-describedby'] = 'inputGroup-sizing-default'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for fname, f in self.fields.items():
            f.widget.attrs['class'] = 'form-control input-lg'
            f.widget.attrs['aria-describedby'] = 'inputGroup-sizing-default'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        for fname, f in self.fields.items():
            f.widget.attrs['class'] = 'form-control input-lg'
            f.widget.attrs['aria-describedby'] = 'inputGroup-sizing-default'

