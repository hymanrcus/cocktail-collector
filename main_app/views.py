from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Drink
from .forms import PresentationForm

def __init__(self, name, description, spirit):
    self.name = name
    self.description = description
    self.spirit = spirit



# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request,):
  return render(request, 'about.html')

def drinks_index(request):
  drinks = Drink.objects.all()
  return render(request, 'drinks/index.html', { 'drinks': drinks })

def drinks_detail(request, drink_id):
  drink = Drink.objects.get(id=drink_id)
  presentation_form = PresentationForm()
  return render(request, 'drinks/detail.html', { 
    'drink': drink, 'presentation_form': presentation_form
    })

class DrinkCreate(CreateView):
  model = Drink
  fields = '__all__'

class DrinkUpdate(UpdateView):
  model = Drink
  fields = '__all__'

class DrinkDelete(DeleteView):
  model = Drink
  success_url = '/drinks/'