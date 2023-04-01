from django.urls import reverse


def node_component(node):
    reference = reverse("menu", kwargs={"menu_name": node.menu_name, "slug": node.slug})
    print(reference)
    node_html = f"""
<li>
    <a href='{reference}'>{node.option}</a>
</li>
"""
    return node_html


def render_menu(tree_dict: dict):
    menu = ""
    for node in list(tree_dict.keys()):
        menu += node_component(node)
        menu += "<ul>"
        menu += render_menu(tree_dict[node]["children"])
        menu += "</ul>"
    return menu
