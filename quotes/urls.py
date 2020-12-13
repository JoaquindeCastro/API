from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.RandomQuoteView.as_view(), name='random'),
]