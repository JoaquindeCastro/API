from rest_framework import serializers

from .models import Issue

class IssueSerializer(serializers.HyperlinkedModelSerializer):
	number = serializers.ReadOnlyField()

	class Meta:
		model = Issue
		fields = ('number', 'title','summary','department','status')