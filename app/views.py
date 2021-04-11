import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

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

def home(request):
    return render(request, "home.html")

def search(request):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    content = "Hello there! " +  "It's " + formatted_now
    return HttpResponse(content)