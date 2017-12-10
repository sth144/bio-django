from django.conf.urls import url

from Data import views

urlpatterns = [
    url(r'^$', views.db, name='db'),
]
