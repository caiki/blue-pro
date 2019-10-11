#from django.conf.urls import patterns, url
#urlpatterns= patterns('Procesos.views', 
#					  url(r'^heart/', 'Depositos_view')
#					 )

#from django.conf.urls import patterns, url
from django.urls import path
from Procesos.views import *
urlpatterns=[ 
			path('heart/',Depositos_view),
			]