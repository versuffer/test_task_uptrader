from django import template
from django.core.cache import cache
from tree_builder.core.cache import cache_menu_query
from tree_builder.core.tree_builder import build_menu_tree
from tree_builder.core.tree_renderer import node_component, render_menu
from tree_builder.models import Node

register = template.Library()


# @register.inclusion_tag('menu_block.html')
# def draw_menu(menu_name: str):

#     return {
#         'url_name': root_node.url_name,
#         'node_name': menu_name,
#         'menu_name': menu_name,
#         'node_children': []
#     }


@register.inclusion_tag('menu_component.html')
def draw_menu(menu_name: str):
    queryset = cache_menu_query(menu_name)
    root_node = queryset.get(parent=None, menu_name=menu_name)
    menu = node_component(root_node)
    return {'menu': menu}
