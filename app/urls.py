from django.urls import path  

from .views import ( 
	ItemDetailView, 
	checkout, 
	HomeView, 
	add_to_cart, 
	remove_from_cart,
	search, 
)

app_name = 'app'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("search/", search, name="search"),
	path('product-page/<slug>/', ItemDetailView.as_view(), name='product'),
	path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'), 
	path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'), 
	path('checkout/', checkout, name='checkout'), 
]