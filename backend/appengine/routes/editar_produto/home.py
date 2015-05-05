# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse
from routes.produtos.home import *

@login_not_required
@no_csrf
def index():
    query = Produtos.query()
    produto_lista = query.fetch()
    form = ProdutosForm()
    produto_lista = [form.fill_with_model(produto) for produto in produto_lista]
    contexto = {'produto_lista':produto_lista}
    editar_form_path = router.to_path(editar_form)
    for produto in produto_lista:
        produto['edit_path'] ='%s/%s'%(editar_form_path,  produto['id'])
    return TemplateResponse(contexto)

@login_not_required
@no_csrf
def editar_form(produtos_id):
    produtos_id = int(produtos_id)
    produtos = Produtos.get_by_id(produtos_id)
    produtos_form = ProdutosForm()
    produtos_form.fill_with_model(produtos)
    contexto = {'salvar_path': router.to_path(editar,  produtos_id),
                'produtos':produtos_form}
    return TemplateResponse(contexto, '/produtos/home.html')

@login_not_required
@no_csrf
def editar(produtos_id, **propriedades):
    produtos_id = int(produtos_id)
    produtos = Produtos.get_by_id(produtos_id)
    produtos_form = ProdutosForm(**propriedades)
    erros = produtos_form.validate()
    if erros:
       contexto = {'salvar_path': router.to_path(salvar),
                   'erros': erros,
                   'produtos' : produtos_form}
       return TemplateResponse(contexto,'/produtos/home.html')
    else:
        produtos_form.fill_model(produtos)
        produtos.put()
        return RedirectResponse(router.to_path('/produtos/home.html'))

