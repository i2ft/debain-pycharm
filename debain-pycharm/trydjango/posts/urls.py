"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import (
posts_detail,
posts_list,
posts_create,
posts_delete,
posts_update
)




urlpatterns = [

    url(r'^$', posts_list),
    url(r'^create/$', posts_create),
    url(r'^detail/(?P<id>\d+)/$', posts_detail),
    url(r'^update/$', posts_update),
    url(r'^delete/$', posts_delete)
]
