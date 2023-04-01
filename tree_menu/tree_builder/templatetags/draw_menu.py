from django import template
from tree_builder.services.cache import cache_menu_query
from tree_builder.services.tree_renderer import node_component, render_menu

register = template.Library()


@register.inclusion_tag("menu_component.html")
def draw_menu(menu_name: str):
    queryset = cache_menu_query(menu_name)
    root_node = queryset.get(parent=None, menu_name=menu_name)
    menu = node_component(root_node)
    return {"menu": menu}
