from django.conf.urls import url
from period import views


urlpatterns = [
    url(r'^checkValue/$', views.checkValue, name='checkValue'),
    url(r'^receive/$', views.receive, name='receive'),
    url(r'^period/$', views.main, name='main'),
    url(r'^$', views.main, name='main'),
    
]   