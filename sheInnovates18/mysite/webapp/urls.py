from django.conf.urls import url
from . import views
from . import googleScript

urlpatterns = [
	url(r'^$', views.index, name='index'), #homepage
	url(r'^gugle$', googleScript.google, name='meowth'),	#gato
	url(r'^photo$', views.index1, name='meowth')	#camera
 
]
