from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodFitnessModel
from .forms import FoodFitnessForm
from django.contrib.auth.models import User


# Create your views here.
# Home page function
def index(request):
    return render(request, 'myApp/index.html')


# Confirmation function
def confirmedUser(request):
    return render(request, 'myApp/confirmedUser.html')


# function to add a new user
def newUser(request):
    form = FoodFitnessForm(request.POST or None)
    context = {
        'form': form
    }
    return render(request, 'myApp/newUser.html', context)


def confirmedUser(request):
    User.objects.create_user(request.POST["username"], request.POST["calories"], request.POST["date"])
    return render(request, 'myApp/confirmedUser.html')
