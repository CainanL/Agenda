from django.contrib import admin
from . models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin): #Para modificar as exibições no painel adminstrativo
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome')  #define quais elementos podem ser clicados
    #list_filter = ('nome', 'sobrenome')  #define quais tipos de filtro vai existir
    list_per_page = 10  #define a quantidade de elemento que será exibido por página
    search_fields = ('nome', 'sobrenome', 'telefone')  #adiciona um campo para busca
    list_editable = ('telefone', 'mostrar')  #campos que podem ser editados diretamente na tabela de exibição

# Register your models here.
#adiciona o model ao painel administrativo do django
admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)  #o ContatoAdmin está indo junto para modificar a tabela de exibição e exibir o nome e o sobrenome