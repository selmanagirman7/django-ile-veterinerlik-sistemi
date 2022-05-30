from django.db import models

# Create your models here.
class ürün(models.Model):
    name = models.CharField(max_length=100 , verbose_name='hayvan ismi')
    description = models.TextField(verbose_name='hakkında')
    image = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    def get_image_path(self):
        return '/img/'+self.image
    