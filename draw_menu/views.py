from django.shortcuts import render
from django.http import Http404
from .templatetags import menu_tags
from .models import Menu

def display_menu(request, menu_name):
    try:
        menu = menu_tags.draw_menu(menu_name)
    except Menu.DoesNotExist:
        raise Http404("Menu does not exist")
    return render(request, 'display_menu.html', {'menu': menu})

def main_page_view(request):
    return render(request, 'mainpage.html')