from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=RCSequence.objects.all(), template_name='ReverseComplement/form.html')),
]
