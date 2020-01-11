from django.contrib import admin
from django.urls import path


from . import views

urlpatterns = [
	path('', views.home, name='news-home'),
	path('scrape/', views.scrape, name='news-scrape'),
	path('search/', views.search, name='search'),
]
