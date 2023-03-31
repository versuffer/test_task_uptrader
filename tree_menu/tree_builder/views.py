from django.shortcuts import render
from .models import Node


def start_page(request):
    menu_list = Node.objects.filter(parent=None)
    return render(request, template_name='base.html', context={'menu_list': menu_list})


def draw_menu(request, menu_name: str, node_id: str):
    menu_nodes = Node.objects.filter(menu_name=menu_name)
    head_node = menu_nodes.get(id=node_id)
    path_nodes = []
    while True:
        path_nodes.append(head_node)
        if head_node.parent:
            head_node = head_node.parent
        else:
            break
    path_nodes = path_nodes[::-1]

    return render(request)
