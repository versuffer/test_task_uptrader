from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tree_builder.urls")),
]

# Debug toolbar
urlpatterns += [
    path("__debug__/", include("debug_toolbar.urls")),
]
