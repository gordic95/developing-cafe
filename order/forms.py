from typing import ClassVar

from django import forms
from .models import *


class OrderForm(forms.ModelForm):
    """Форма для создания нового заказа."""
    class Meta:
        model: ClassVar[type[Order]] = Order
        fields: list[str] = ['menu_order', 'table_number']
        error_messages = {'table_number': {'unique': 'Такой стол уже занят', 'invalid': 'Некорректный номер стола', 'required': 'Введите номер стола'}}


