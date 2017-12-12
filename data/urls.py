from django.conf.urls import url

from Data import views

urlpatterns = [
    # not used currently
    url(r'^$', ListView.as_view(queryset=DNASeq.objects.all(), template_name='data/dnaupload.html')),
]
