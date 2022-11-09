from django.shortcuts import render
from django.http import HttpResponse

class Drink:
  def __init__(self, name, description, spirit):
    self.name = name
    self.description = description
    self.spirit = spirit

drinks= [
  Drink('Martini', 'Traditional', 'Gin'),
  Drink('Daiquiri', 'Fruity', 'Rum'),
  Drink('Mule', 'Refreshing', 'Vodka'),
  Drink('Sour', 'Complex', 'Bourbon')
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Welcome to the bar</h1>')

def about(request,):
  return render(request, 'about.html')

def drinks_index(request):
  return render(request, 'drinks/index.html', { 'drinks': drinks })