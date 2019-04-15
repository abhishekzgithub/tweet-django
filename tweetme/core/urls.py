from django.urls import include, path
from . import views
from .routing import routee


urlpatterns=[
    path('', views.index, name="index"),
    path('api/',include(routee.urls)),
]