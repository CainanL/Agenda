from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat  #para unir campos para fazer buscas
from django.contrib import messages

# Create your views here.


def index(request):    
    # faz uma consulta sql com todos os dadados da tabela contatos
    # caso eu queria que ordene em ordem decrecente eu passo o "-" antes do argumento ('-nome')
    contatos = Contato.objects.order_by('-id').filter(mostrar=True)

    # para criar uma paginação -> para criar os botões das páginas (<- 2, 3, 4,... ->) deve ser implementado no html
    paginator = Paginator(contatos, 5)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        # informações que serão passadas para as views
        'contatos': contatos
    })

    # argumento que foi enviado pela url entre <tipo:argumento>
# def ver_contato(request, contato_id):
#     try:
#         contato = Contato.objects.get(id=contato_id)  #busca todos os elementos onde o id é igual ao contatato_id
#         return render(request, 'contatos/ver_contato.html', {
#             'contato':contato  #é enviado para o html
#         })
#     except Contato.DoesNotExist as e:
#         raise Http404  #forma crua para corrigir pania não existente


def ver_contato(request, contato_id):
    # faz com que busque pelo id, caso o id não exista, ele gera um error 404
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        raise Http404()  # se o contato não pode ser exibido, ele lança o erro falando que não existe a página para aquele contato

    return render(request, 'contatos/ver_contato.html', {
        'contato': contato  # é enviado para o html
    })


def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        messages.add_message(request, messages.ERROR, 'O campo de pesquisa não pode estar vazio.') # envia uma mensagem para o index
        return redirect('index')  # redireciona o usuário para a view index

    campos = Concat('nome', Value(' '), 'sobrenome')

    contatos = Contato.objects.annotate(  #para fazer buscas mais complexas, ex: nome e sobrenome juntos
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)  #o nome ou telefone deve conter o termo da busca
    )

    # contatos = Contato.objects.order_by('-id').filter(
    #     Q(nome__icontains=termo) | Q(sobrenome__icontains=termo),  # __icontains == like %%; Q(argumento) | Q(argumento) -> diz que pode ser um ou outro
    #     mostrar=True,
    # )

    paginator = Paginator(contatos, 5)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })
