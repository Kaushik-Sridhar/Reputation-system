# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from myapp.models import User,Article

admin.site.register(User)
admin.site.register(Article)

# Create your views here.

def hello(request):
	string="Hello!"
	text=["mon","tue","wed","thur","fri"]
	return render(request,"myapp/hello.html",{"string":string,"text":text})

def hello1(request):
	string="Hello1!!!"
	return HttpResponse(string)

def article(request,year,month):
	string = "Displaying %s,%s" %(year,month)
	return HttpResponse(string)

class comment(TemplateView):
	template_name="myapp/hello.html"
	 
def whoispub(request): #returns the one with highest reputaion as the publisher
	all_articles=Article.objects.all()
	for article in all_articles:
		article.user.repu+=article.upvote-article.downvote
		article.user.save()
	all_user=User.objects.all()
	x=-99999
	for user in all_user:
		if(user.repu>x):
			x=user.repu
			string='The publisher is ' + user.name
	
	return HttpResponse(string)

	
	
