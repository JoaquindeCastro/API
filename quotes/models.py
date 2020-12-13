from django.db import models

class Quote(models.Model):
	text = models.TextField()
	author = models.CharField(max_length=255)
	source = models.URLField(blank=True, null=True)
	theme = models.CharField(blank=True, null=True, max_length=255)

	def __str__(self):
		return f'{self.word_count}, {self.letter_count}, {self.author}'

	@property
	def word_count(self):
		return len(self.text.split())

	@property
	def letter_count(self):
		letters = [i for i in self.text if i.isalpha()]
		return len(letters)
	
	