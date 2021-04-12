from django.urls import path 
from app import views 

from .views import ( 
	# ItemDetailView, 
	# checkout, 
	HomeView, 
	# add_to_cart, 
	# remove_from_cart,
	# search, 
	# search_and_show, 
	# OrderSummaryView
)

app_name = 'app'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("search/", views.search, name="search"),
]