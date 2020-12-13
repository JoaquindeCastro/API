import random

from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import QuoteSerializer
from .models import Quote

class RandomQuoteView(generics.RetrieveAPIView):

	serializer_class = QuoteSerializer

	def get_object(self):
		queryset = Quote.objects.all()

		# possible params => author, min_letters, min_words, max_letters, max_words

		author = self.request.query_params.get('author', None)
		if author is not None:
			queryset = queryset.filter(author=author)

		min_letters = self.request.query_params.get('min_letters', None)
		if min_letters is not None and min_letters.isnumeric():
			queryset = [x for x in queryset if x.letter_count>=int(min_letters)]

		min_words = self.request.query_params.get('min_words', None)
		if min_words is not None and min_words.isnumeric():
			queryset = [x for x in queryset if x.word_count>=int(min_words)]

		max_letters = self.request.query_params.get('max_letters', None)
		if max_letters is not None and max_letters.isnumeric():
			queryset = [x for x in queryset if x.letter_count<=int(max_letters)]

		max_words = self.request.query_params.get('max_words', None)
		if max_words is not None and max_words.isnumeric():
			queryset = [x for x in queryset if x.word_count<=int(max_words)]

		try:
			query = random.choice(queryset)
		except:
			return None

		return query

class PostQuoteView(APIView):

	serializer_class = QuoteSerializer

	def post(self, request, format=None):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			text = serializer.data.get('text')
			author = serializer.data.get('author')
			queryset = Quote.objects.filter(text=text)
			if queryset.exists():
				quote = queryset[0]
				quote.author = author
				quote.save(update_fields=['author'])
			else:
				quote = Quote(text=text, author=author)
				quote.save()

			return Response(self.serializer_class(quote).data, status=status.HTTP_201_CREATED)

class QuoteViewSet(viewsets.ModelViewSet):
	queryset = Quote.objects.all()
	serializer_class = QuoteSerializer
