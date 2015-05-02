# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaecookie.decorator import no_csrf
from gaeforms.ndb.form import ModelForm
from gaegraph.model import Node
from gaepermission.decorator import login_not_required
from config.template_middleware import TemplateResponse
from tekton import router
from routes.produtos.home import *

@login_not_required
@no_csrf
def index():
    query = Produtos.query()
    produto_lista = query.fetch()
    form = ProdutosForm()
    produto_lista = [form.fill_with_model(produto) for produto in produto_lista]
    contexto = {'produto_lista':produto_lista}
#    produto_lista = [form.fill_with_model(produto) for produto in produto_lista]
#    editar_form_path = router.to_path(editar_form)
#    for produto in produto_lista:
#        produto['edit_path'] ='%s/%s'%(editar_form_path,produto['id'])
    return TemplateResponse(contexto)

#def editar_form(produtos_id):
#   contexto = {'salvar_path': router.to_path(editar)}
#    return TemplateResponse(contexto,'/produtos')

#def editar(**propriedades):
#    produtos_form = ProdutosForm(**propriedades)
#    erros = produtos_form.validate()
#    if erros:
#       contexto = {'salvar_path': router.to_path(index),
#                   'erros': erros,
#                   'produtos' : produtos_form}
#       return TemplateResponse(contexto,'/produtos/home.html')
#    else:
#        produtos=produtos_form.fill_model()
#        produtos.put()
#        return RedirectResponse(router.to_path('/produtos'))