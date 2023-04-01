from django.urls import path

from .views import draw_menu, start_page

urlpatterns = [
    path("", start_page, name="start"),
    path("<str:menu_name>/<slug:slug>", draw_menu, name="menu"),
]
