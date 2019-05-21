# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    # The home page
    url(r'tour/([0-9]+)/$' , views.tour , name='tour'),
    url(r'^$', views.index, name='index'),

]


