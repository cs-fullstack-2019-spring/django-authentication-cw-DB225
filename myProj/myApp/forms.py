from django import forms
from .models import FoodFitnessModel

# Form for the new user to create
class FoodFitnessForm(forms.ModelForm):
    class Meta:
        model = FoodFitnessModel
        fields = '__all__'
