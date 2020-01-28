from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import UserAccount
from .models import UserAccount
# Create your views here.
def register(request):
	if request.method == 'POST':
		name = request.POST['Name']
		username = request.POST['email']
		pass1 = request.POST['password1']
		pass2 = request.POST['password2']
		if pass1==pass2:
			if User.objects.filter(username=username).exists():
				messages.info(request,'username already registered')
				return redirect('register')
			else:
				user = User.objects.create_user(password=pass1,username=username,first_name=name,email=username)
				user.save()
				return redirect('/')
		else:
			messages.info(request,'Password not matching')
			return redirect('register')
	else:
		return render(request,'account/register.html')

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			messages.error(request,'invalid credentials')
			return redirect('login')
	else:
		print('user')
		return render(request,'account/login.html')

def logout(request):
	auth.logout(request)
	return redirect('login')
