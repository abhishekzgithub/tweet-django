from django.conf.urls import url, include
from . import views
from django.urls import path
from django.contrib.auth import views as auth_view
urlpatterns=[
    path('',views.user_home,name="home"),
    url(r'^login/',auth_view.LoginView.as_view(template_name='login.html'),name="login"),
    url(r'^logout/',views.user_logout,name="logout"),
    url(r'^signup/',views.user_signup,name="signup"),
]