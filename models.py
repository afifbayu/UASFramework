from django.db import models

# Create your models here.
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        app_label = 'crud_app' 

    def __str__(self):
        return self.name