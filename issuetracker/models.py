from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model

User = get_user_model()

class Department(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

STATUS_CHOICES = [
	('Open', 'Open'),
	('Closed', 'Closed'),
]

def get_unique_number():
	number = get_random_string(length=6, allowed_chars='1234567890')
	while Issue.objects.filter(number=number).exists():
		number = get_random_string(length=6, allowed_chars='1234567890')
	return number

class Issue(models.Model):
	number = models.IntegerField(default=get_unique_number, unique=True)
	title = models.CharField(max_length=255)
	summary = models.TextField()
	department = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, blank=True)
	assigned = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
	status = models.CharField(max_length=255, choices=STATUS_CHOICES)

	def __str__(self):
		return f'#{self.number} - {self.title}'
