from rest_framework import serializers

from .models import Fact, Question

class FactSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Fact
		fields = ('content','category','tags')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Fact
		fields = ('question','answer','category','tags')