from .cache import cache_menu_query


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

        # Seeking parent node in queryset without hitting database
        for check_node in queryset:
            if check_node.id == parent_id:
                parent_node = check_node

        recursive_build(parent_node, tree_dict)

    # Hit database or get cached data for building menu tree
    queryset = cache_menu_query(menu_name)

    # Run building
    menu_dict = {}

    # Seeking active node in queryset without hitting database
    for check_node in queryset:
        if check_node.slug == slug:
            active_node = check_node

    recursive_build(active_node)
    return menu_dict
