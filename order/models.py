from django.db import models

from order.constants import STATUS_TYPES


class Menu(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название блюда") #Название блюда
    price = models.PositiveIntegerField(verbose_name="Цена") #Цена

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"


class Order(models.Model):
    table_number = models.PositiveIntegerField(unique=True, verbose_name="Номер стола")  #Номер столика
    menu_order = models.ManyToManyField(Menu, verbose_name="Меню заказа", related_name="menu_order") #Блюдо
    status = models.CharField(max_length=1, default='0', choices=STATUS_TYPES, verbose_name="Статус заказа")  #Статус заказа
    res = 0

    def total_price(self):
        total = 0
        for object in self.menu_order.all():
            total += object.price
        return total


    def get_absolute_url(self):
        return f'/order/{self.id}/'

    def __str__(self):
        return f"Заказ №{self.table_number}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['table_number']


