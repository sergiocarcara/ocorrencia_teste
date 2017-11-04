# -*- coding: utf8 -*-
from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from ckeditor.fields import RichTextField

#local de armazenamento das imagens
fs = FileSystemStorage(location='media/')

# Create your models here.
'''class Categoria(models.Model):
    nome_categoria = models.CharField('Nome da Categoria', max_length=20)
    sigla = models.CharField('Sigla da Categoria', max_length=3)
    descricao = models.TextField('Descrição da categoria')

    def __str__(self):
        return '{}'.format(self.nome_categoria)'''


#tabela para noticiar policia
class Poster(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    fonte = models.CharField(max_length=200)
    imagen = models.ImageField(storage=fs)
    texto = RichTextField()
    data_criacao = models.DateTimeField('Data de Criação', default=timezone.now)
    data_publicacao = models.DateTimeField('Data de Publicação', blank=True, null=True)

    def publicacao(self):

        self.data_publicacao = timezone.now
        self.save()

    def __str__(self):
        return self.titulo

    class Meta:
        ordering= ('-data_publicacao',)

#tabela para noticiar politica
class Poster_polit(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    fonte = models.CharField(max_length=200)
    imagen = models.ImageField(storage=fs)
    texto = RichTextField()
    data_criacao = models.DateTimeField('Data de Criação', default=timezone.now)
    data_publicacao = models.DateTimeField('Data de Publicação', blank=True, null=True)

    def publicacao(self):

        self.data_publicacao = timezone.now
        self.save()

    def __str__(self):
        return self.titulo

    class Meta:
        ordering= ('-data_publicacao',)

#tabela para noticiar classificado
class Classificado(models.Model):
    titulo = models.CharField(max_length=200)
    fonte  = models.CharField(max_length=200)
    imagen = models.ImageField(storage=fs)
    texto  = RichTextField()
    data_criacao = models.DateTimeField('Data de Criação', default=timezone.now)
    data_publicacao = models.DateTimeField('Data de Publicação', blank=True, null=True)

    def publicacao(self):

        self.data_publicacao = timezone.now
        self.save()

    def __str__(self):
        return self.titulo


