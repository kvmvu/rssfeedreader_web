"""rssfeedreader_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path

from apps.core.views import index, rest_feeds, rest_feeds_detail, rest_items

urlpatterns = [
    path('', index, name='index'),
    path('feeds/', rest_feeds, name='rest-feeds'),
    re_path(r'^feeds/(?P<pk>[0-9]*)/$', rest_feeds_detail, name="rest-feeds-detail"),
    path('items/', rest_items, name="rest-items"),
    path('admin/', admin.site.urls),
]
