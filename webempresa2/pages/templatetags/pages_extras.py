# Lo primero es registrarlo dentro de la librería de Templates
from atexit import register
from django import template
from pages.models import Page

# Creamos variable para hacer referencia a la librería template.
register = template.Library()

# Conseguir la lista de páginas

@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages
