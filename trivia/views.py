import random

from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import FactSerializer, QuestionSerializer
from .models import Fact, Question

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
