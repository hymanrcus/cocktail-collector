from django.forms import ModelForm
from .models import Presentation

class PresentationForm(ModelForm):
  class Meta:
    model = Presentation
    fields = ['color', 'garnish']