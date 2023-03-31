from django.urls import path
from .views import start_page, draw_menu

urlpatterns = [
    path('', start_page),
    path('<str:menu_name>/<int:node_id>', draw_menu),
]
