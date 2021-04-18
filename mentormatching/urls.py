from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.Assign.as_view(), name='assign-matches'),
]