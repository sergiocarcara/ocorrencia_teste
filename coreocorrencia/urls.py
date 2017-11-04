from django.conf.urls import  url
from coreocorrencia import views

urlpatterns = [
    url(r'^$',views.home),
    url(r'^policia_poster/$',views.policia),
    url(r'^politica_poster/$',views.politica),
    url(r'^classificado/$',views.classificado),
    #url(r'^contato/$', views.contato),
    url(r'^policia_detalhes/(?P<id_poster>\d+)/$',views.policia_detalhes),
    url(r'^politica_detalhes/(?P<id_poster>\d+)/$',views.politica_detalhes),

]

