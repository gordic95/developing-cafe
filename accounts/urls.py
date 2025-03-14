from django.urls import path
from . views import *




app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
    path('register/', RegisterView, name='register'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/orders/', profile_order_view, name='profile_orders'),
]

