# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaecookie.decorator import no_csrf
from gaeforms.ndb.form import ModelForm
from gaegraph.model import Node
from gaepermission.decorator import login_not_required
from config.template_middleware import TemplateResponse
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse

class Produtos(Node):
    nome = ndb.StringProperty(required=True)
    titulo = ndb.StringProperty(required=True)#required = true significa que é obrigatório
    descricao = ndb.StringProperty(required=True)
    imagem = ndb.StringProperty(required=True)
    preco = ndb.StringProperty(required=True)

class ProdutosForm(ModelForm):
    _model_class = Produtos
    _include = [Produtos.nome, Produtos.titulo, Produtos.descricao, Produtos.imagem,Produtos.preco]

@login_not_required
@no_csrf
def index(**propriedades):
    produtos_form = ProdutosForm(**propriedades)
    erros = produtos_form.validate()
    if erros:
       contexto = {'salvar_path': router.to_path(index),
                   'erros': erros,
                   'produtos' : produtos_form}
       return TemplateResponse(contexto,'/produtos/home.html')

    else:
        produtos=produtos_form.fill_model()

        produtos.put()


        return RedirectResponse(router.to_path('/produtos'))
        #feito para mostrar o que esta sendo salvo no banco



