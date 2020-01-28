from django.shortcuts import render
from food.models import *

# Create your views here.
def index(request):
    Dish = Dishes.objects.all()
    print(Dish[0].image)
    return render(request,'index.html',{'Dishes':Dish})