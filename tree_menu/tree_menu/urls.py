from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('tree_builder.urls')),
    path('admin/', admin.site.urls),
]

# Debug toolbar
urlpatterns += [
    path('__debug__/', include('debug_toolbar.urls')),
]