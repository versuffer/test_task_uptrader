from django.core.cache import cache
from tree_builder.models import Node


def build_menu_tree(menu_name: str, slug: str):
    def recursive_build(node, path_node_dict=None):
        nonlocal queryset, menu_dict
        path_node_dict = path_node_dict or {None: None}
        tree_dict = {node: {"children": {}}}

        for child_node in queryset:
            if child_node.parent_id == node.id:
                path_node = list(path_node_dict.keys())[0]
                if child_node == path_node:
                    tree_dict[node]["children"].update(path_node_dict)
                else:
                    tree_dict[node]["children"].update({child_node: {"children": {}}})

        parent_id = node.parent_id
        if parent_id is None:
            menu_dict = tree_dict
            return

        parent_node = queryset.get(id=parent_id)
        recursive_build(parent_node, tree_dict)

    # Hit database or get cached data for building menu tree
    queryset = cache.get(f"{menu_name}_queryset")
    if queryset is None:
        queryset = Node.objects.filter(menu_name=menu_name)
        cache.set(f"{menu_name}_queryset", queryset, timeout=86400)

    # Run building
    menu_dict = {}
    active_node = queryset.get(slug=slug)
    recursive_build(active_node)
    return menu_dict
