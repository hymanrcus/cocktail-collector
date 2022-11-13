from django.db import models
from django.urls import reverse


GARNISHES= (
  ('E', 'Edible'),
  ('F', 'Flower'),
  ('S', 'Sugar')
)


# Create your models here.
class Drink(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  spirit = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('drinks_detail', kwargs={'drink_id': self.id})

class Presentation(models.Model):
  color = models.CharField(max_length=10)
  garnish = models.CharField(
    max_length=10,
    choices=GARNISHES,
    default=GARNISHES[0][0]
  )
  drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_garnish_display()} is {self.color}"