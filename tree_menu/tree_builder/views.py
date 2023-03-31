from django.shortcuts import render
from .models import Node


def start_page(request):
    pass


def draw_menus(request, node_id: str):
    queryset = Node.objects.all()

    pass
