from django.core.cache import cache
from django.shortcuts import redirect, render, reverse
from tree_builder.core.tree_builder import build_menu_tree
from tree_builder.core.tree_renderer import render_menu

from .models import Node


def start_page(request):
    return render(request, template_name='index.html')


def draw_menu(request, menu_name: str, url_name: str):
    queryset = cache.get('node_queryset')
    if queryset is None:
        queryset = Node.objects.all()
        cache.set('node_queryset', queryset, timeout=86400)
    menu_nodes = queryset.filter(menu_name=menu_name)

    try:
        if (int(url_name),) in menu_nodes.values_list('id'):
            url_name = menu_nodes.get(id=url_name).url_name
            return redirect(
                reverse(
                    'menu', kwargs={'menu_name': menu_name, 'url_name': url_name}
                )
            )
    except ValueError:
        pass

    head_node = menu_nodes.get(url_name=url_name)
    path_nodes = []

    while True:
        path_nodes.append(head_node)
        if head_node.parent:
            head_node = head_node.parent
        else:
            break
    root_node = path_nodes[-1]
    return render(
        request,
        template_name='menu_page.html',
        context={
            'node_children': root_node.children.all(),
            'path_nodes': path_nodes,
            'menu_name': menu_name,
            'url_name': root_node.url_name,
        }
    )


def draw(request, menu_name: str, url_name: str):
    menu = render_menu(build_menu_tree(menu_name, url_name))
    return render(request, template_name='menu_page.html', context={'menu': menu})
