from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page_view),
    path('<str:menu_name>/', views.display_menu, name='display_menu'),
]