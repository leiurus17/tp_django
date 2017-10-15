from django.conf.urls import include, url

urlpatterns = [url(r'^hello/', 'ube.views.hello', name = 'hello'),]