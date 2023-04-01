from django.contrib import admin

from .models import Node


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    exclude = ("slug",)
    list_display = ["id", "menu_name", "option", "parent"]
