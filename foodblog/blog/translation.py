from modeltranslation.translator import translator, TranslationOptions
from .models import Catagory, Recipe, Tag

class RecipeTranslationOptions(TranslationOptions):
    fields = ('title',  'short_description', 'description')


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', )
    
    
class TagTranslationOptions(TranslationOptions):
    fields = ('title',)
    
        
translator.register(Recipe, RecipeTranslationOptions)
translator.register(Catagory, CategoryTranslationOptions)
translator.register(Tag, TagTranslationOptions)