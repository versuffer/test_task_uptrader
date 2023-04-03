from django.urls import path

from .views import CheckMenuNameView, CheckPrimaryKeyView, DrawMenuView, StartPageView

urlpatterns = [
    path("", StartPageView.as_view(), name="start"),
    path("<str:menu_name>/", CheckMenuNameView.as_view(), name="menu_redirect"),
    path("<str:menu_name>/<int:pk>", CheckPrimaryKeyView.as_view(), name="pk_redirect"),
    path("<str:menu_name>/<slug:slug>", DrawMenuView.as_view(), name="menu"),
]
