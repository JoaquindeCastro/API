from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.RandomQuoteView.as_view(), name='random'),
	path('post', views.PostQuoteView.as_view(), name='post')
]