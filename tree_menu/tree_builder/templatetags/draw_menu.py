from django import template
from tree_builder.models import Node
from django.core.cache import cache


register = template.Library()


@register.inclusion_tag('menu_block.html')
def draw_menu(menu_name: str):
    queryset = cache.get('node_queryset')
    if queryset is None:
        queryset = Node.objects.all()
        cache.set('node_queryset', queryset, timeout=86400)
    root_node = queryset.get(parent=None, menu_name=menu_name)
    return {
        'url_name': root_node.url_name,
        'node_name': menu_name,
        'menu_name': menu_name,
        'node_children': []
    }
