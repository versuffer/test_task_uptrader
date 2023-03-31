from django.contrib import admin
from .models import Node
from django.utils.text import slugify


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'url_name', 'menu_name', 'option', 'parent']
    list_filter = ['id', 'parent']
