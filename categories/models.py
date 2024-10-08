from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    # parent FK pointing to itself
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name
