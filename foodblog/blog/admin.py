from django.contrib import admin
from .models import Comment,Recipe,Tag,Catagory
# Register your models here.

admin.site.register(Comment)
admin.site.register(Recipe)
admin.site.register(Tag)
admin.site.register(Catagory)