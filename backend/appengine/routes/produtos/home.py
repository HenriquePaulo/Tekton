# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaecookie.decorator import no_csrf
from gaeforms import base
from gaeforms.base import Form
from gaeforms.ndb.form import ModelForm
from gaegraph.model import Node
from gaepermission.decorator import login_not_required
from config.template_middleware import TemplateResponse
from tekton import router


class Produtos(Node):
    titulo = ndb.StringProperty(required=True)#required = true significa que é obrigatório
    descricao = ndb.StringProperty(required=True)
    imagem = ndb.StringProperty(required=True)
    preco = ndb.StringProperty(required=True)

class ProdutosForm(ModelForm):
    _model_class = Produtos
    _include = [Produtos.titulo, Produtos.descricao, Produtos.imagem,Produtos.preco]

@login_not_required
@no_csrf
def index(_resp, **propriedades):
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
        _resp.write(propriedades)

        #feito para mostrar o que esta sendo salvo no banco



