from django.conf.urls import url
from period import views


urlpatterns = [
    url(r'^$', views.main, name='main'),
]   