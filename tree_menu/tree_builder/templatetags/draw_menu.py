from django import template
from tree_builder.models import Node


register = template.Library()


@register.inclusion_tag('node_component.html')
def draw_menu(menu_name: str):
    root_node = Node.objects.get(
        parent=None, menu_name=menu_name
    )
    return {
        'node_id': root_node.id, 'node_name': menu_name, 'menu_name': menu_name}
