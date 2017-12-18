from django.conf.urls import url
from . import views


# Url patterns for this app

urlpatterns = [

	# Not used in current deployment
    url(r'^$', ListView.as_view(queryset=RCSequence.objects.all(), template_name='ReverseComplement/form.html')),

]
