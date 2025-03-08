from django import forms
from .models import *


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['menu_order', 'table_number']


class DeleteForm(forms.Form):
    class Meta:
        model = Order
        fields = ['id']