from django.urls import path

from .views import draw, draw_menu, start_page

urlpatterns = [
    path('', start_page, name='start'),
    path('<str:menu_name>/<str:url_name>', draw, name='menu'),
]
