import random

from django.core.mail import send_mail

from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import FactSerializer, QuestionSerializer
from .models import Fact, Question

from django.conf import settings

def send_trivia_email():
	trivia = random.choice(Fact.objects.all())
	send_mail(trivia.uid,trivia.content,settings.EMAIL_HOST,[settings.EMAIL_HOST])

class RandomFactView(generics.RetrieveAPIView):

	serializer_class = FactSerializer

	def get_object(self):
		queryset = Fact.objects.all()

		try:
			query = random.choice(queryset)
		except:
			return None

		return query

class RandomQuestionView(generics.RetrieveAPIView):

	serializer_class = QuestionSerializer

	def get_object(self):
		queryset = Question.objects.all()

		try:
			query = random.choice(queryset)
		except:
			return None

		return query

class PostFactView(APIView):

	serializer_class = FactSerializer

	def post(self, request, format=None):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			content = serializer.data.get('content')
			category = serializer.data.get('category',None)
			tags = serializer.data.get('tags',None)
			fact = Fact.objects.create(content=content,category=category,tags=tags)
			fact.save()

			return Response(self.serializer_class(fact).data, status=status.HTTP_201_CREATED)

class TriviaEmailView(APIView):

	def post(self,request,format=None):
		pwd = request.query_params.post('pwd', None)
		if pwd == 'hjdgjwerifj49':
			#category = request.query_params.post('cartegory', None)
			send_trivia_email()

'''
if 'uid' in serializer.data:
	update_fields = []
	uid = serializer.data.get('uid')
	fact = Fact.objects.get(uid=uid)
	
	fact.save(update_fields=update_fields)
'''