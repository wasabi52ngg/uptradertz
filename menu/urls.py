from django.urls import path, re_path
from .views import MenuTemplateView
from django.contrib import admin

urlpatterns = [
    re_path(r'^menu/(?P<menu_name>[\w-]+)/$', MenuTemplateView.as_view(), name='menu_root'),
    re_path(r'^menu/(?P<menu_name>[\w-]+)/?(?P<path>.+)/$', MenuTemplateView.as_view(), name='menu_item'),
]