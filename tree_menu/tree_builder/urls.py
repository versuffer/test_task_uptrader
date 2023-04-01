from django.urls import path

from .views import DrawMenuView, StartPageView

urlpatterns = [
    path("", StartPageView.as_view(), name="start"),
    path("<str:menu_name>/<slug:slug>", DrawMenuView.as_view(), name="menu"),
]
