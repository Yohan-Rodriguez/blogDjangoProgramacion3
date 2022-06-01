# -*- coding: utf-8 -*-
"""
Created on Tue May 31 05:21:48 2022

@author: ASUS
"""

from django.urls import path
from .views  import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
        #path('post/<int:pk>/update', UpdateDetailView.as_view(), name='post_update'),
        path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='post_delete'),
        path('post/edit/<int:pk>/', BlogUpdateView.as_view(), name='post_edit'),
        path('post/new/', BlogCreateView.as_view(), name='post_new'),
        path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
        path('', BlogListView.as_view(), name='home'),
]