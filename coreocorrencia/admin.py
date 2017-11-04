from django.contrib import admin
from coreocorrencia.models import *

# Register your models here.

class Poster_admin(admin.ModelAdmin):
    list_display = ('autor','titulo','data_criacao','data_publicacao')
    search_fields = ['autor']

class Poster_polit_admin(admin.ModelAdmin):
    list_display = ('autor','titulo','data_criacao','data_publicacao')
    search_fields = ['autor']

class Classificado_admin(admin.ModelAdmin):
    list_display = ('titulo','data_criacao','data_publicacao')
    search_fields = ['titulo']


admin.site.register(Poster, Poster_admin)
admin.site.register(Poster_polit, Poster_polit_admin)
admin.site.register(Classificado, Classificado_admin)