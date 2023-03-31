from django.core.cache import cache


def cached_queries(request):
    return {'cache': cache.get('node_queryset')}
