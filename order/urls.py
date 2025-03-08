from django.urls import path
from .views import CreateOrderView, main, OrderDeleteView, OrderListView, OrderUpdateView, OrderUpdateMenuView, \
    money_of_the_day, OrderDeleteOnIdView

app_name = 'order'




urlpatterns = [
    path('', main, name='main'),
    path('create_order/', CreateOrderView.as_view(), name='create_order'),
    path('delete_order/<int:pk>/', OrderDeleteView.as_view(), name='delete_order'),
    path('order_list/', OrderListView.as_view(), name='order_list'),
    path('update_order/<int:pk>/', OrderUpdateView.as_view(), name='update_order'),
    path('update_menu/<int:pk>/', OrderUpdateMenuView.as_view(), name='update_menu'),
    path('money_of_the_day/', money_of_the_day, name='money_of_the_day'),

    path('delete_order_on_id/<int:pk>/', OrderDeleteOnIdView.as_view(), name='delete_order_on_id'),

]