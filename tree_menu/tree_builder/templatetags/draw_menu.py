from django import template
from tree_builder.models import Node
from django.core.cache import cache


register = template.Library()


@register.inclusion_tag('node_component.html')
def draw_menu(menu_name: str):
    queryset = Node.objects.all()
    cache.set('node_queryset', queryset)
    root_node = queryset.get(parent=None, menu_name=menu_name)
    return {
        'url_name': root_node.url_name, 'node_name': menu_name, 'menu_name': menu_name}
