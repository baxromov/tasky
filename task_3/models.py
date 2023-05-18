from django.db import models


class Status(models.TextChoices):
    START = 'start'
    IN_PROCESS = 'in_process'
    FINISH = 'finish'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    status = models.CharField(choices=Status.choices, default=Status.START)
    file = models.FileField(upload_to='file', null=True)
