"""second URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from secapp import views
from django.urls import re_path as url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    url('index', views.index, name="index"),
    url('about', views.about, name="about"),
    url('contact', views.contact, name="contact"),
    url('course_details', views.course_details, name="course-details"),
    url('courses', views.courses, name="courses"),
    url('events', views.events, name="events"),
    url('pricing', views.pricing, name="pricing"),
    url('trainers', views.about, name="trainers"),
]
