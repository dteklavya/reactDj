"""django_twitter_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url

from django_twitter_project import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^$', views.index),
    path('admin/', admin.site.urls),
    url('twitter_oauth/', include('django_twitter_auth.urls')),
    url('twitter/', include('django_twitter_mining.urls')),
    url(r'^logout/$', views.logout),
]
