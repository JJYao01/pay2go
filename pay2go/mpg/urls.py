from django.conf.urls import url
from mpg import views


urlpatterns = [
    url(r'^/checkValue/$', views.checkValue, name='checkValue'),
    url(r'^mpg/$', views.main, name='mpg'),
    url(r'^$', views.main, name='main'),
    
]   