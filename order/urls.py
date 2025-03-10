from django.urls import path
from .views import CreateOrderView, OrderDeleteView, OrderListView, OrderUpdateView, OrderUpdateMenuView, \
    money_of_the_day, order_search_by_id, OrderDetailView

app_name = 'order'




urlpatterns = [
    path('create_order/', CreateOrderView.as_view(), name='create_order'),
    path('delete_order/<int:pk>/', OrderDeleteView.as_view(), name='delete_order'),
    path('', OrderListView.as_view(), name='order_list'),
    path('update_order/<int:pk>/', OrderUpdateView.as_view(), name='update_order'),
    path('update_menu/<int:pk>/', OrderUpdateMenuView.as_view(), name='update_menu'),
    path('money_of_the_day/', money_of_the_day, name='money_of_the_day'),
    path('order_list/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('order_search/', order_search_by_id, name='order_search'),
]