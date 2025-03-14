from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    search_fields = ['user']


admin.site.register(Profile, ProfileAdmin)