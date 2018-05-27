from django.conf.urls import include,url
from views import hello1,article,comment,whoispub


urlpatterns = [
	url(r'^hello/$', hello1 , name='hello1'),
	url(r'^article/(?P<year>\d{4})/(?P<month>\d{2})' , article , name='article'),
	url(r'^comment/$', comment.as_view(), name='comment'),
	url(r'^whoispublisher/$' , whoispub , name='publisher'),

]
