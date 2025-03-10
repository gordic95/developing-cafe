from typing import ClassVar

from django import forms
from .models import *


class OrderForm(forms.ModelForm):
    """Форма для создания нового заказа."""
    class Meta:
        model: ClassVar[type[Order]] = Order
        fields: list[str] = ['menu_order', 'table_number']
        error_messages = {'table_number': {'unique': 'Такой стол уже занят', 'invalid': 'Некорректный номер стола', 'required': 'Введите номер стола'}}


    def clean_table_number(self):
        table_number = self.cleaned_data.get('table_number')

        if table_number == 0:
            raise forms.ValidationError("Номер стола не может быть равен нулю.")

        return table_number
