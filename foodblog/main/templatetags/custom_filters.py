from django.template import Library

register = Library()

@register.filter
def turncate(text,count):
    sentences = text.split('.')[:int(count)]
    return  '.'.join(sentences) + "."
    