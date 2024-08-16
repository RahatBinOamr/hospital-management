from django.db import models
from tinymce.models import HTMLField  
from autoslug import AutoSlugField
# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    image = models.ImageField(upload_to='department', null=True)
    name = models.CharField(max_length=200)
    description = HTMLField()
    d_slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name
