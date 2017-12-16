from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views
import form.views
import ReverseComplement.views
import ComputeGC.views
import ConsensusSequence.views
import BaseDistribution.views
import Transcriber.views
import Translator.views
import HammingDistance.views
import ParamFibo.views
import ParseMotif.views
import ProbabilityDom.views
import Data.views                                   # Had to capitalize for Heroku

# Examples:
# url(r'^$', 'engine.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', Data.views.db, name='db'),
    url(r'^form', form.views.HomeView.as_view(), name='form'),
    url(r'^reversecomplement', ReverseComplement.views.HomeView.as_view(), name='form'),
    url(r'^computegc', ComputeGC.views.HomeView.as_view(), name='form'),
    url(r'^consensussequence', ConsensusSequence.views.HomeView.as_view(), name='form'),
    url(r'^basedistribution', BaseDistribution.views.HomeView.as_view(), name='form'),
    url(r'^transcriber', Transcriber.views.HomeView.as_view(), name='form'),
    url(r'^translator', Translator.views.HomeView.as_view(), name='form'),
    url(r'^hammingdistance', HammingDistance.views.HomeView.as_view(), name='form'),
    url(r'^paramfibo', ParamFibo.views.HomeView.as_view(), name='form'),
    url(r'^parsemotif', ParseMotif.views.HomeView.as_view(), name='form'),
    url(r'^probabilitydom', ProbabilityDom.views.HomeView.as_view(), name='form'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dnaupload', Data.views.DNAView.as_view(), name='form'),
    url(r'^rnaupload', Data.views.RNAView.as_view(), name='form'),
    url(r'^peptideupload', Data.views.PeptideView.as_view(), name='form')
]
