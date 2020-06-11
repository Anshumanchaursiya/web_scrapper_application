from django.urls import path
from django.conf.urls import url,include

from . import views



urlpatterns = [

	path('', views.base, name='base'),
	path('blog_list/',views.blog_list,name='blog_list'),
	
    
]
