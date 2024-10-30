from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    path('',views.home, name="home"),
    path('blog_list', views.blog_list, name="blog_list"),
    path('resource_details', views.resource_details, name="resource_details")
]
