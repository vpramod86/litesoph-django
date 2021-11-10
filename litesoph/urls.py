from typing import ValuesView
from django.urls import path

from . import views

# app_name = "litesoph"
urlpatterns = [
   path('', views.index, name="index"),
   path('about', views.about, name="about"),
   path('features', views.features, name="features"),
   path('resources', views.resources, name="resources"),
   path('github', views.github, name="github"),
   path('gui', views.gui, name="gui"),
   path('people', views.people, name="people"),
   path('contact', views.contact, name="contact"),
   path('news', views.news, name="news"),
   path('faq', views.faq, name="faq"),
   path('publications', views.publications, name="publications"),
   path('visualization',views.visualization, name="visualization"),
   path('download', views.download, name="download"),
   path('resources/manual', views.manual, name="manual"),
   path('resources/tutorials', views.tutorials, name="tutorials"),
   path('resources/tools', views.tools, name="tools"),
]
