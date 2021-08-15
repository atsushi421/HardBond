from django.db import models
from django.contrib.auth import get_user_model


class Result(models.Model):
    user_name = models.CharField(
        max_length=255,
        default='名無し',
        blank=False,
        null=False,
    )
    
    name = models.CharField(
        max_length=255,
        default='Bonta',
        blank=False,
        null=False
    )
    
    result = models.IntegerField(
        default=0,
        blank=False,
        null=False,
    )