from django.template import Library
from blog.models import Catagory

register = Library()

@register.simple_tag
def get_catagories():
    return Catagory.objects.all()