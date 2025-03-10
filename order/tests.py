from django.test import TestCase
from . models import Order, Menu
from . filters import OrderFilter
from . forms import OrderForm
from . views import *
import pytest


@pytest.fixture # фикстура для создания объекта Order
def create_order():
    """Фикстура для создания объекта Order."""
    return Order.objects.create(table_number=1, status='new')

@pytest.mark.django_db # тест для создания объекта Order
def test_order(create_order):
    """Тестирование объекта Order."""
    order = create_order
    assert order.table_number == 1
    assert order.status == 'new'


@pytest.fixture # фикстура для создания объекта Menu
def create_menu():
    """Фикстура для создания объекта Menu."""
    return Menu.objects.create(name='burger', price=100)

@pytest.mark.django_db
def test_menu(create_menu): # тест для создания объекта Menu
    """Тестирование объекта Menu."""
    menu = create_menu
    assert menu.name == 'burger'
    assert menu.price == 100


@pytest.fixture # фикстура для создания объекта OrderFilter
def create_order_filter():
    """Фикстура для создания объекта OrderFilter."""
    # return OrderFilter('id=1')
    a = Order.objects.create(table_number=1, status=1)
    return OrderFilter(a)


@pytest.mark.django_db # тест для фильтрации объектов Order
def test_order_filter(create_order_filter):
    """Тестирование объекта OrderFilter."""
    order_filter = create_order_filter
    print(f'ВОТ ТУТ {order_filter.__dict__}')
    assert order_filter


@pytest.fixture # фикстура для создания объекта OrderForm
def create_order_form():
    """Фикстура для создания объекта OrderForm."""
    return OrderForm({'menu_order': 'burger', 'table_number': 1})

@pytest.mark.django_db
def test_order_form(create_order_form):
    """Тестирование объекта OrderForm."""
    order_form = create_order_form
    assert order_form


@pytest.fixture # фикстура для создания объекта OrderView
def create_order_view():
    """Фикстура для создания объекта OrderView."""
    return OrderListView.as_view()

@pytest.mark.django_db
def test_order_view(create_order_view):
    """Тестирование объекта OrderView."""
    order_view = create_order_view
    assert order_view


