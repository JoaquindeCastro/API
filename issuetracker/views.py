import random

from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import IssueSerializer
from .models import Issue

class AddIssueView(generics.CreateAPIView):
	serializer_class = IssueSerializer
	queryset = Issue.objects.all()

class GetIssueView(generics.RetrieveAPIView):
	serializer_class = IssueSerializer
	permission_classes = [IsAuthenticated]

	def get_object(self):
		queryset = Issue.objects.all()

		number = self.request.query_params.get('number', None)

		if number is None:
			return None

		issue = Issue.objects.get(number=number)

		return issue

class UpdateIssueView(generics.UpdateAPIView):
	serializer_class = IssueSerializer
	permission_class = [AllowAny]
	queryset = Issue.objects.all()
	lookup_field = 'number'