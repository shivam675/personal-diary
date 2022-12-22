from django import forms
from .models import MyLogEntry

class LogForm(forms.ModelForm):
  class Meta:
    model = MyLogEntry
    fields = ["description","intresting"]
    labels = {"description": "Day's Log", "intresting": " Intresting"}