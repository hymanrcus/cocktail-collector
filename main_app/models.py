from django.db import models
from django.urls import reverse

# Create your models here.
class Drink(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  spirit = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('drinks_detail', kwargs={'drink_id': self.id})