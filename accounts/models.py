from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    first_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Фамилия')
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name='Возраст')
    phone = models.CharField(max_length=12, null=True, blank=True, verbose_name='Телефон')
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name='Email')
    avatar = models.ImageField(null=True, blank=True, upload_to='avatars/', default='avatars/1.jpg', verbose_name='Аватар')
    orders = models.ManyToManyField('order.Order', null=True, blank=True, related_name='orders', verbose_name='Заказы')
    from_city = models.CharField(max_length=100, null=True, blank=True, verbose_name='Город')




    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


