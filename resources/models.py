from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Group(models.Model):
	name = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return self.name

class Resource(models.Model):
	name = models.CharField(max_length=30)
	link = models.URLField()
	description = models.TextField()
	group = models.ForeignKey(Group)

	def __str__(self):
		return self.name