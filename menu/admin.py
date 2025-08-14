from django.contrib import admin
from .models import MenuItem


# Register your models here.


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu_name', 'parent', 'url', 'order')
    list_filter = ('menu_name',)
    search_fields = ('title', 'url')
    ordering = ('menu_name', 'order')
