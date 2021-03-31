from django.db import models
import random

def generate_unique_id():
	length = 6

	while True:
		code = ''.join(random.choices([str(n) for n in range(10)],k=6))
		if Fact.objects.filter(uid=code).exists() or Question.objects.filter(uid=code).exists():
			continue
		else:
			break

	return code

class Fact(models.Model):
	uid = models.CharField(max_length=6, default=generate_unique_id, unique=True)
	content = models.TextField()
	category = models.CharField(max_length=63)
	tags = models.CharField(max_length=128)

class Question(models.Model):
	uid = models.CharField(max_length=6, default=generate_unique_id)
	question = models.TextField()
	answer = models.TextField()
	category = models.CharField(max_length=63)
	tags = models.CharField(max_length=128)
