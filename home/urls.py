from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("", views.index, name="home"),
    path("contact.html", views.contact, name="contact"),
    path("about.html", views.about, name="about"),
    path("blog.html",views.blog, name="blog" )
    ]