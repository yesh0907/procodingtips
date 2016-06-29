from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Series(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Tip(models.Model):
	title = models.CharField(max_length=30)
	author = models.CharField(max_length=30, default="")
	resources = models.TextField(default="")
	body = models.TextField()
	pub_date = models.DateField()
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(default=0)
	order = models.IntegerField(default=1)
	series = models.ForeignKey(Series)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['order']