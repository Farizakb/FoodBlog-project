from django.contrib import admin
from .models import Comment,Recipe,Tag,Catagory
from modeltranslation.admin import TranslationAdmin

class NewsAdmin(TranslationAdmin):
    pass


# Register your models here.

admin.site.register(Comment)
admin.site.register(Recipe,NewsAdmin)
admin.site.register(Tag,NewsAdmin)
admin.site.register(Catagory,NewsAdmin)