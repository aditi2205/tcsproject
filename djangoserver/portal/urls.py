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
    url(r'^analysis/', views.analysis, name='analysis'),
    url(r'^stories/', views.stories, name='stories'),
    url(r'^story/new/$', views.story_new, name='story_new'),
]
