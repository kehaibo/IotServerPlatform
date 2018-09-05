from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^UserLogin/$', views.UserLogin,name='UserLogin'),
 	url(r'^home/$', views.hello,name='home'),
]