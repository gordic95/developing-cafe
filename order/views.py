from django.contrib import messages
from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DeleteView, ListView, UpdateView


from .filters import OrderFilter
from .models import Order
from .forms import OrderForm, DeleteForm


def main(request):
    return render(request, 'order/main.html', {})


class CreateOrderView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/create_order.html'
    success_url = reverse_lazy('order:order_list')


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order/order_delete.html'
    success_url = reverse_lazy('order:order_list')


class OrderDeleteOnIdView(DeleteView):
    model = Order
    form_class = DeleteForm
    template_name = 'order/delete_order_on_id.html'
    success_url = reverse_lazy('order:order_list')


class OrderListView(ListView):
    model = Order
    template_name = 'order/order_list.html'
    context_object_name = 'order_list'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = OrderFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class OrderUpdateView(UpdateView):
    model = Order
    fields = ['status']
    template_name = 'order/order_update.html'
    success_url = reverse_lazy('order:order_list')


class OrderUpdateMenuView(UpdateView):
    model = Order
    fields = ['menu_order']
    template_name = 'order/order_update.html'
    success_url = reverse_lazy('order:order_list')


def money_of_the_day(request):
    queryset = Order.objects.filter(status='1')
    money = 0
    count = 0
    for i in queryset:
        for j in i.menu_order.all():
            money += j.price
            count += 1
    return render(request, 'order/money_of_the_day.html', context={'money': money})











