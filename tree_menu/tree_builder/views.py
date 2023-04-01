from django.shortcuts import render
from tree_builder.core.tree_builder import build_menu_tree
from tree_builder.core.tree_renderer import render_menu


def start_page(request):
    return render(request, template_name="index.html")


def draw_menu(request, menu_name: str, url_name: str):
    menu = render_menu(build_menu_tree(menu_name, url_name))
    return render(request, template_name="menu_page.html", context={"menu": menu})
