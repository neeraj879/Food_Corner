from django.shortcuts import render
from cart.models import Cart,CartItem
from food.models import Dishes
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def view(request):
    cart = Cart.objects.all()
    return render(request,'cart/cart.html',{'carts':cart})

def update_cart(request,id,quantity=1):
    dish=Dishes.objects.get(id=id)
    cart=Cart(request)
    #cart.add(dish,dish.price)
    return HttpResponseRedirect(reverse('cart/'))