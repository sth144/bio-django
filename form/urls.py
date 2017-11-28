from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Blurb.objects.all(), template_name='form/form.html')),
]