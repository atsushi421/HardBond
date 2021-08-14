from django.db import models

class Result(models.Model):
    name = models.CharField(
        max_length=255,
        default='名無し',
        blank=False,
        null=False
    )
    
    result = models.IntegerField(
        default=0,
        blank=False,
        null=False,
    )