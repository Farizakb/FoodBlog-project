from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    img = models.ImageField('Sekil',upload_to = 'user', null = True,blank = True),
    bio = models.TextField('Bio', null = True,blank = True),
    
    