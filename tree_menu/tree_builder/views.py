from django.urls import reverse
from django.views.generic.base import RedirectView, TemplateView
from tree_builder.services.cache import cache_menu_query
from tree_builder.services.tree_builder import build_menu_tree
from tree_builder.services.tree_renderer import render_menu

from .models import Node


class StartPageView(TemplateView):
    template_name = "index.html"


class CheckMenuNameView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        menu_name = kwargs["menu_name"]
        queryset = cache_menu_query(menu_name=menu_name)
        try:
            root_node_slug = queryset.get(parent=None).slug
            return reverse(
                "menu", kwargs={"menu_name": menu_name, "slug": root_node_slug}
            )
        except Node.DoesNotExist:
            pass


class CheckPrimaryKeyView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        menu_name = kwargs["menu_name"]
        queryset = cache_menu_query(menu_name=menu_name)
        try:
            slug = queryset.get(pk=kwargs["pk"]).slug
            return reverse("menu", kwargs={"menu_name": menu_name, "slug": slug})
        except Node.DoesNotExist:
            pass


class DrawMenuView(TemplateView):
    template_name = "menu_page.html"

    def get_context_data(self, **kwargs):
        context = {
            "menu": render_menu(build_menu_tree(kwargs["menu_name"], kwargs["slug"]))
        }
        return context
