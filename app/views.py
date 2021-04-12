import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Book, OrderItem, Order, Author, Publisher, Warehouse

from django.contrib.auth import (
    authenticate, 
    get_user_model, 
    login, 
    logout)

from app.forms import UserLoginForm, UserRegisterForm, SearchForm

# Create your views here.
def login_view(request):
	next = request.GET.get('next')
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		if next:
			return redirect(next)
		return redirect('/')

	context = {
		'form': form, 
	}
	return render(request, "login.html", context)

def register_view(request):
	next = request.GET.get('next')
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(request)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username, password=password)
		login(request, new_user)
		if next:
			return redirect(next)
		return redirect('/')

	context = {
		'form': form, 
	}
	return render(request, "signup.html", context)

class HomeView(ListView):
	model = Book
	template_name = "home.html"

def search(request):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    content = "Hello there! " +  "It's " + formatted_now
    return HttpResponse(content)