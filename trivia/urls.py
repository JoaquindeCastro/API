from django.urls import path, include
from . import views

urlpatterns = [
	path('fact', views.RandomFactView.as_view(), name='random_fact'),
	path('fact/post',views.PostFactView.as_view(),name='post_fact'),
	path('question', views.RandomQuestionView.as_view(), name='random_question'),
	path('fact/email',views.TriviaEmailView.as_view(),name='trivia_email')
]