from django.db import models

# Create your models here.


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        abstract = True
        

class Contact(AbstractModel):
    name = models.CharField('Adiniz',max_length = 50)
    email = models.EmailField('Mailiniz',max_length = 50)
    subject = models.CharField('Movzu',max_length = 250)
    message = models.TextField('Mesajiniz')
    
    class Meta:
        verbose_name = "Elaqe"
        verbose_name_plural = "Elaqeler"
        ordering = ('created_at',)
    
    
    def __str__(self) -> str:
        return f"{self.name}  {self.email}" 


# cat backup.sql | docker exec -i e0f03c33a4d4 psql -U Fariz -d Blog