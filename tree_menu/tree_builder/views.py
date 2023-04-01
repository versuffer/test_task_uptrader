from django.views.generic.base import TemplateView
from tree_builder.services.tree_builder import build_menu_tree
from tree_builder.services.tree_renderer import render_menu


class StartPageView(TemplateView):
    template_name = "index.html"


class DrawMenuView(TemplateView):
    template_name = "menu_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = render_menu(
            build_menu_tree(kwargs["menu_name"], kwargs["slug"])
        )
        return context
