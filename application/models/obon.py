from django.db import models
from . import User
from django.urls import reverse_lazy

class Obon(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )
    
    name = models.CharField(
        max_length=255,
        default='Bonta',
        blank=True,
        null=False,
    )
    
    money = models.IntegerField(
        default=1000,
    )
    
    image = models.ImageField(
        default='bonta.png',
        blank=False,
    )
    
    material = models.CharField(
        max_length=255,
        default='wood'
        )
    
    size = models.IntegerField(
        default=5,
        )
    
    wise = models.IntegerField(
        default=5,
        )
    
    weight = models.IntegerField(
        default=5,
        )
    
    motivation = models.IntegerField(
        default=5,
        )
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy("index")