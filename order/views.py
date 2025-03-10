from typing import ClassVar


from django.db import models
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView

from .filters import OrderFilter
from .models import Order
from .forms import OrderForm


class CreateOrderView(CreateView):
    """Представление для создания нового заказа."""
    model: ClassVar[type[Order]] = Order
    form_class: type[OrderForm] = OrderForm
    template_name: str = 'order/create_order.html'
    success_url: str = reverse_lazy('order:order_list')


class OrderDeleteView(DeleteView):
    """Представление для удаления заказа."""
    model: ClassVar[type[Order]] = Order
    template_name: str = 'order/order_delete.html'
    success_url: str = reverse_lazy('order:order_list')


def order_search_by_id(request):
    """Представление для поиска заказа по ID и удаления его по ID."""
    if request.method == 'GET':
        order_id = request.GET.get('order_id')
        if order_id:
            try:
                order = Order.objects.get(id=order_id)
                orders = [order]
            except Order.DoesNotExist:
                orders = []
        else:
            orders = []


    # POST запрос, для удаления заказа по ID
    elif request.method == 'POST':
        order_id = request.POST.get('order_id')
        print(order_id)
        if order_id:
            try:
                order = Order.objects.get(id=order_id)
                order.delete()  # Удаляем заказ
                orders = []
            except Order.DoesNotExist:
                orders = []
        else:
            orders = []
    else:
        orders = []

    return render(request, 'order/order_search.html', {'orders': orders})


class OrderListView(ListView):
    """Представление для отображения списка заказов."""
    model: ClassVar[type[Order]] = Order
    template_name: str = 'order/order_list.html'
    context_object_name: str = 'order_list'
    paginate_by: int = 3


    def get_queryset(self: 'OrderListView', **kwargs) -> models.QuerySet:
        queryset = super().get_queryset()
        self.filterset = OrderFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self: 'OrderListView', **kwargs: 'OrderListView') -> dict[str, ClassVar[type[OrderFilter]]]:
        context = super().get_context_data(**kwargs)
        context['filterset']: ClassVar[type[OrderFilter]] = self.filterset
        return context


class OrderUpdateView(UpdateView):
    """Представление для обновления статуса заказа."""
    model: ClassVar[type[Order]] = Order
    fields: list[str] = ['status']
    template_name: str = 'order/order_update.html'
    success_url: str = reverse_lazy('order:order_list')


class OrderUpdateMenuView(UpdateView):
    """Представление для изменения меню заказа."""
    model: ClassVar[type[Order]] = Order
    fields: list[str] = ['menu_order']
    template_name: str = 'order/order_update_menu.html'
    success_url: str = reverse_lazy('order:order_list')


def money_of_the_day(request):
    """Представление для расчета суммы всех заказов."""
    queryset= Order.objects.filter(status='1')
    money = 0 # Общая сумма всех заказов
    count = 0 # Количество заказов
    for i in queryset:
        for j in i.menu_order.all():
            money += j.price
            count += 1
    return render(request, 'order/money_of_the_day.html', context={'money': money, 'count': count})


class OrderDetailView(DetailView):
    """Представление для отображения деталей заказа."""
    model: ClassVar[type[Order]] = Order
    template_name: str = 'order/order_detail.html'
    context_object_name: str = 'order'












