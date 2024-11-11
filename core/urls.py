from django.contrib import admin
from django.urls import path,include
from . import views 
app_name = 'core'

urlpatterns = [
    path('',views.home, name="home"),
    path('article_list', views.article_list, name="article_list"),
    # Define the article detail URL pattern
    path('article_detail/<int:id>', views.article_detail, name='article_detail'),
    path('resource_details', views.resource_details, name="resource_details")
]
