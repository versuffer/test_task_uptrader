from django.shortcuts import render
from django.core.cache import cache
from .models import Node


def start_page(request):
    return render(request, template_name='base.html')


def draw_menu(request, menu_name: str, url_name: str):
    queryset = cache.get('node_queryset')
    if not queryset:
        queryset = Node.objects.all()
        cache.set('node_queryset', queryset)
    menu_nodes = queryset.filter(menu_name=menu_name)
    head_node = menu_nodes.get(url_name=url_name)
    path_nodes = []

    while True:
        path_nodes.append(head_node)
        if head_node.parent:
            head_node = head_node.parent
        else:
            break

    return render(
        request, template_name='menu_block.html', context={
            'node_children': path_nodes[-1].children.all(), 'path_nodes': path_nodes,
        }
    )
