import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Book, OrderItem, Order, Author, Publisher, Warehouse
from django.db import models

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
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
        
		allBooks = Book.objects.all()
		authors_to_book = set()
		for book in allBooks:
			authors_to_book.add(book.author.get())
        
		context['author_to_book'] = authors_to_book

		return context

def search(request):
	authors = Author.objects.all()
	authors_list = {}
	for e in authors:
		firstname = e.firstname
		lastname = e.lastname
		key1 = firstname.lower()
		key2 = lastname.lower()
		if key1 not in authors_list:
			authors_list[key1] = (firstname, lastname)
		if key2 not in authors_list:
			authors_list[key2] = (firstname, lastname)
		
	books = Book.objects.all()
	book_list = {}
	isbn_list = {}
	pub_list = {}
	for e in books:
		title = e.title.lower()
		lst = title.split(" ")
		for i in lst: 
			if i not in book_list:
				book_list[i] = [e.title]
			else: 
				book_list[i].append(e.title)
		val = e.ISBN
		isbn = "".join(val.split("-"))
		pub_val = e.publisher.name.lower()
		pub_val = pub_val.split()
		
		if isbn not in isbn_list:
			isbn_list[isbn] = e.ISBN
		if pub_val[0] not in pub_list:
			pub_list[pub_val[0]] = e.publisher.name

	query = request.GET.get("query")
	val = query.strip()
	queries = val.split(" ") 
	vals = [q.lower() for q in queries]
	
	for q in vals:
		if q in authors_list: 
			first, last = authors_list[q]
			author = get_object_or_404(Author, firstname=first, lastname=last)
			book = Book.objects.filter(author=author)
			if book.exists():
				context = {
					'books': book
				}
				return render(request, "book_list.html", context)

		if q in book_list:
			titles = book_list[q]
			book = []
			for title in titles:
				book.append(Book.objects.filter(title=title))
			if book:
				context = {
					'books': book[0]
				}
				return render(request, "book_list.html", context)

		if q in pub_list:
			pub = pub_list[q]
			p = get_object_or_404(Publisher, name=pub)
			book = Book.objects.filter(publisher=p)
			if book.exists():
				context = {
					'books': book
				}
				return render(request, "book_list.html", context)

		if q in isbn_list:
			isbn_val = isbn_list[q]
			book = Book.objects.filter(ISBN=isbn_val)
			if book.exists():
				context = {
					'books' : book
				}
				return render(request, "book_list.html", context)

		else: 
			context = {}
	return render(request, "book_list.html", context)



def search_and_show(request, slug):
	form = SearchForm(request.POST or None)
	if form.is_valid():
		first = form.cleaned_data.get('firstname')
		last = "Mayer"
		author = get_object_or_404(Author, firstname=first, lastname=last)
		book = Book.objects.filter(author=author)
		if True:
			context = {
				'books': [book]
			}
			return render(request, "book_list.html", context)
		else: 
			return redirect("bookstore:home", slug=slug)
	return render(request, "book_list.html")