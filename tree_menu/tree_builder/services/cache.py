from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from tree_builder.models import Node


def cache_menu_query(menu_name):
    queryset = cache.get(f"{menu_name}_queryset")
    if queryset is None:
        queryset = Node.objects.filter(menu_name=menu_name).select_related("parent")
        cache.set(f"{menu_name}_queryset", queryset, timeout=86400)
    return queryset


def refresh_cache(instance):
    cache.delete(f"{instance.menu_name}_queryset")


@receiver(post_save, sender=Node)
def post_save(sender, instance, **kwargs):
    refresh_cache(instance)


@receiver(post_delete, sender=Node)
def post_delete(sender, instance, **kwargs):
    refresh_cache(instance)
