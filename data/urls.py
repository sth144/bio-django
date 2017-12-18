from django.conf.urls import url

from Data import views


# Url patterns for this app
urlpatterns = [

    # not used in current deployment
    url(r'^$', ListView.as_view(queryset=DNASeq.objects.all(), template_name='data/dnaupload.html')),

]
