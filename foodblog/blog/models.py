from audioop import reverse
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from main.models import AbstractModel


User = get_user_model()


# Create your models here.
class Catagory(AbstractModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'catagory')
    
    class Meta:
        ordering = ('created_at',)


    def __str__(self):
        return self.title

class Tag(AbstractModel):
    title = models.CharField(max_length=100)
    
    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.title
    
    
class Recipe(AbstractModel):
    author = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'recipe',)
    catagory = models.ForeignKey(Catagory,on_delete = models.CASCADE,related_name = 'recipe')
    tags = models.ManyToManyField(Tag)
    
    title = models.CharField(max_length = 100,db_index =True)
    short_description = models.CharField(max_length = 255)
    description = models.TextField()
    image = models.ImageField(upload_to = 'recipe')
    cover_image = models.ImageField(upload_to = 'recipe')
    
    
    class Meta:
        verbose_name = ('Resept')
        verbose_name_plural = ('Reseptler')
        ordering = ('created_at',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy("recipe_det", kwargs={"pk": self.id})
    
    
    
    
class Story(AbstractModel):
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'story')
    tags = models.ManyToManyField(Tag)
    
    title = models.CharField(max_length = 100, db_index = True)
    short_description = models.CharField(max_length = 255)
    description = models.TextField()
    image = models.ImageField(upload_to = 'story')
    cover_image = models.ImageField(upload_to = 'story')
    
    
    class Meta:
        verbose_name = ('Hekaye')
        verbose_name_plural = ('Hekayeler')
        ordering = ('created_at',)
        
    def __str__(self):
        return self.title
    
    
class Comment(AbstractModel):
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null= True,blank = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name = 'comment')
    recipe = models.ForeignKey(Recipe,on_delete = models.CASCADE, related_name = 'comment')
    
    review = models.CharField(max_length=255)
    
    
    class Meta:
        verbose_name = ('Yorum')
        verbose_name_plural = ('Yorumlar')
        ordering = ('-created_at',)