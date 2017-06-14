from django.conf.urls import url

#from . import views

from portal import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^quiz1/', views.FillInfo.as_view(), name='quiz1'),
    url(r'^quiz/', views.quiz, name='quiz'),

    url(r'^analysis/', views.analysis, name='analysis'),
    url(r'^forum/', views.forum, name='forum'),
]
