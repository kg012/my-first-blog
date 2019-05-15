#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 01:59:39 2019

@author: kg
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]