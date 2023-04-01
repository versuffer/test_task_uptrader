from django.core.cache import cache
from tree_builder.models import Node


def cache_menu_query(menu_name):
    queryset = cache.get(f"{menu_name}_queryset")
    if queryset is None:
        queryset = Node.objects.filter(menu_name=menu_name)
        cache.set(f"{menu_name}_queryset", queryset, timeout=86400)

    return queryset
