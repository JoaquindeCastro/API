from rest_framework import serializers

from .models import Fact, Question

class FactSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Fact
		fields = ('uid', 'content','category','tags')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Fact
		fields = ('uid', 'question','answer','category','tags')