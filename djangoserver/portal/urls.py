from django.conf.urls import url

#from . import views

from portal import views
from .views import ContactWizard
from .forms import DetailsForm,Quiz

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^quiz1/',ContactWizard.as_view([DetailsForm,Quiz])),
    #url(r'^quiz1/', views.FillInfo, name='quiz1'),
    #url(r'^quiz1/quiz/', views.letsplay, name='quiz'),
    #url(r'^quiz/quizres', views.quizres, name='quiz'),
    url(r'^analysis/', views.analysis1, name='analysis1'),
    url(r'^analysis2/', views.analysis2, name='analysis2'),
    url(r'^analysis3/', views.analysis3, name='analysis3'),
    url(r'^analysis4/', views.analysis4, name='analysis4'),
    url(r'^analysis5/', views.analysis5, name='analysis5'),
    url(r'^analysis6/', views.analysis5, name='analysis6'),
    url(r'^stories/', views.stories, name='stories'),
    url(r'^story/new/$', views.story_new, name='story_new'),
]
