from django.contrib import admin
from .models import Node


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'menu_name', 'option', 'parent']
    list_filter = ['id', 'parent']

    def save_model(self, request, obj, form, change):
        if obj.parent:
            obj.menu_name = obj.parent.menu_name
        super().save_model(request, obj, form, change)