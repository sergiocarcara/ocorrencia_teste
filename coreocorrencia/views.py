# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponse
from django.utils import timezone
#from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404
from coreocorrencia.models import Poster
from coreocorrencia.models import Poster_polit
from coreocorrencia.models import Classificado



# Create your views here.
def home(request):
    poster = Poster.objects.all()[:1]
    posts_politica = Poster_polit.objects.all()[:1]
    posts = Classificado.objects.all()[:2]
    return render (request, 'index.html',{
        'poster': poster,
        'posts_politica': posts_politica,
        'posts': posts
        })

def policia(request):
    posts = Poster.objects.filter()
    return render (request, 'policia_poster.html', {'posts':posts})

def classificado(request):
    posts = Classificado.objects.filter()
    return render (request, 'classificado.html', {'posts':posts})

def politica(request):
    posts_politica = Poster_polit.objects.filter()
    return render (request, 'politica_poster.html', {'posts_politica':posts_politica})

def policia_detalhes(request, id_poster):
    poster= Poster.objects.all()[:10]#limita a quantidade de informação do banco
    poster_detalhes = get_object_or_404(Poster, pk=id_poster)
    return render (request, 'policia_poster_detalhes.html', {
        'poster_detalhes':poster_detalhes,
        'poster': poster
        })

def politica_detalhes(request, id_poster):
    poster= Poster_polit.objects.all()[:10]#limita a quantidade de informação do banco
    politicas_detalhes = get_object_or_404(Poster_polit, pk=id_poster)
    return render (request, 'politica_poster_detalhes.html', {
        'politicas_detalhes':politicas_detalhes,
        'poster': poster
        })



