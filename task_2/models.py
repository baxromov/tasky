from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    def __str__(self):
        return self.name
