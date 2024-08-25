from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    deadline = models.DateField()

    class Status(models.TextChoices):
        COMPLETED = 'Complete'
        PROGRESSING = 'Progressing'
    
    status = models.CharField(
      max_length=15,
      choices=Status,
      default=Status.PROGRESSING
    )
