from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('tree_builder.urls')),
    path('admin/', admin.site.urls),
]
