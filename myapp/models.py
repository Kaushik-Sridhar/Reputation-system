# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	name=models.CharField(max_length=20)
	email=models.CharField(max_length=20)
	phone=models.IntegerField()
	domain=models.CharField(max_length=20,default="Author")
	repu=models.IntegerField(default=0)

	class Meta:
		db_table="user"
	
	def __str__(self):
		return self.name

class Article(models.Model):
	user=models.ForeignKey('User',on_delete=models.CASCADE)
	a_name=models.CharField(max_length=50)
	upvote=models.IntegerField()
	downvote=models.IntegerField()

	class Meta:
		db_table="article"

	def __str__(self):
		return self.a_name
