from django.contrib import admin
from .models import Order, Menu

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'table_number', 'status']
    list_filter = ['status']
    search_fields = ['table_number']

class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Order, OrderAdmin)
admin.site.register(Menu, MenuAdmin)

# Register your models here.
