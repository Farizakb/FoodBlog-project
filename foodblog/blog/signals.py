from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Recipe
from slugify import slugify
from datetime import datetime


@receiver(pre_save,sender=Recipe)
def slug_generation_recipe(sender,instance, **kwargs):
    if instance.slug.split("-slug-")[0] != slugify(instance.title) or instance.slug is None:
        
        instance.slug = slugify(instance.title + ' slug ' +  datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f'))
    
        print(instance.slug)

    