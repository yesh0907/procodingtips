from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tip(models.Model):
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=255, default="")
	resources = models.TextField(default="")
	body = models.TextField()
	pub_date = models.DateTimeField()

	def __str__(self):
		return self.title